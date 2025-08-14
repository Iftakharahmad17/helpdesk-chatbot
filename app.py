
from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

app = Flask(__name__)

MODEL_NAME = "distilgpt2"
_device = 0 if torch.cuda.is_available() else -1

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=_device)

SYSTEM_PREFIX = (
    "You are a polite and helpful helpdesk assistant for IT/software topics. "
    "Answer concisely and avoid making up facts. "
    "If unsure, ask a short clarifying question.\n\n"
)

def generate_reply(user_message: str) -> str:
    prompt = SYSTEM_PREFIX + "User: " + user_message.strip() + "\nAssistant:"
    out = generator(
        prompt,
        max_new_tokens=80,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )[0]["generated_text"]
    reply = out.split("Assistant:")[-1].strip()
    reply = reply.replace("\n\n", "\n").split("User:")[0].strip()
    if not reply:
        reply = "I'm here to help. Could you please rephrase your question?"
    return reply

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_message = (data or {}).get("message", "").strip()
    if not user_message:
        return jsonify({"reply": "Please type a message."})
    try:
        reply = generate_reply(user_message)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"An error occurred while generating a reply: {e}"}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False)
