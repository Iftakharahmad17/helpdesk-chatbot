
(function(){
  const key='theme';
  const toggle=document.getElementById('themeToggle');
  const setTheme = (val)=>{document.documentElement.dataset.theme=val; localStorage.setItem(key,val); toggle.textContent = val==='dark' ? '☀️' : '🌙';};
  setTheme(localStorage.getItem(key)||'dark');
  toggle.addEventListener('click',()=> setTheme((document.documentElement.dataset.theme==='dark')?'light':'dark'));

  const chatWindow = document.getElementById('chatWindow');
  const input = document.getElementById('msgInput');
  const sendBtn = document.getElementById('sendBtn');

  function appendMessage(sender, text){
    const wrap = document.createElement('div');
    wrap.className = 'message ' + (sender === 'You' ? 'user' : 'bot');
    wrap.innerHTML = '<div class="meta">'+sender+'</div>' + text.replace(/\n/g,'<br>');
    chatWindow.appendChild(wrap);
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  function send(){
    const msg = input.value.trim();
    if(!msg) return;
    appendMessage('You', msg);
    input.value='';

    const placeholder = document.createElement('div');
    placeholder.className = 'message bot';
    placeholder.innerHTML = '<div class="meta">Bot</div>…';
    chatWindow.appendChild(placeholder);
    chatWindow.scrollTop = chatWindow.scrollHeight;

    fetch('/chat', {
      method: 'POST',
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify({message: msg})
    })
    .then(r=>r.json())
    .then(data=>{
      placeholder.remove();
      appendMessage('Bot', data.reply || 'No reply.');
    })
    .catch(err=>{
      placeholder.remove();
      appendMessage('Bot', 'Error contacting server.');
    });
  }

  sendBtn.addEventListener('click', send);
  input.addEventListener('keydown', e=>{
    if(e.key === 'Enter'){ send(); }
  });
})();
