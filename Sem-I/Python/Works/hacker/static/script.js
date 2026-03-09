// Matrix rain canvas
(function() {
  const canvas = document.getElementById('matrix');
  const ctx = canvas.getContext('2d');

  function resize() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    columns = Math.floor(canvas.width / fontSize);
    drops = new Array(columns).fill(0).map(() => Math.floor(Math.random() * -40));
  }

  const charset = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@$%#*+-/\\|';
  const fontSize = 16;
  let columns = 0;
  let drops = [];

  window.addEventListener('resize', resize);
  resize();

  function draw() {
    // translucent background for trailing effect
    ctx.fillStyle = 'rgba(0, 0, 0, 0.08)';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    ctx.font = `${fontSize}px Consolas, Monaco, monospace`;

    for (let i = 0; i < columns; i++) {
      const x = i * fontSize;
      const y = drops[i] * fontSize;

      // head (bright)
      ctx.fillStyle = '#aaffdd';
      ctx.fillText(charset[Math.floor(Math.random() * charset.length)], x, y);

      // tail (dim)
      ctx.fillStyle = '#1b6';
      ctx.fillText(charset[Math.floor(Math.random() * charset.length)], x, y - fontSize);

      // move drop down
      drops[i] += Math.random() < 0.7 ? 1 : 0; // random pause for variation

      // reset off-screen
      const off = Math.floor(canvas.height / fontSize) + Math.floor(Math.random() * 20);
      if (drops[i] > off) drops[i] = Math.floor(Math.random() * -40);
    }

    requestAnimationFrame(draw);
  }

  draw();
})();

// Typing intro
(function() {
  const intro = document.getElementById('intro');
  const lines = [
    '// ACCESS NODE: OMEGA-GATEWAY',
    'Initializing secure link...',
    'Negotiating ciphersuite [AES-256/GCM]...',
    'Syncing time with NTP shadows...',
    'Bypassing deep packet inspection...',
    'Injecting ephemeral keys...',
    'Access granted. Welcome, Operative.'
  ];

  let i = 0;
  function typeLine(line, cb) {
    let j = 0;
    const timer = setInterval(() => {
      intro.textContent += line[j];
      j++;
      if (j >= line.length) {
        clearInterval(timer);
        intro.textContent += '\n';
        if (cb) setTimeout(cb, 220);
      }
    }, 18);
  }

  function next() {
    if (i >= lines.length) return;
    typeLine(lines[i], () => {
      i++;
      next();
    });
  }

  next();
})();


