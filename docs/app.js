(function () {
  var root = document.documentElement, body = document.body;
  var state = {};
  try { state = JSON.parse(localStorage.getItem('ferc') || '{}'); } catch (_) {}
  function save() { try { localStorage.setItem('ferc', JSON.stringify(state)); } catch (_) {} }

  var aa = document.getElementById('aa');
  if (aa) {
    aa.setAttribute('aria-pressed', root.classList.contains('big') ? 'true' : 'false');
    aa.addEventListener('click', function () {
      var on = root.classList.toggle('big');
      aa.setAttribute('aria-pressed', on ? 'true' : 'false');
      state.big = on; save();
    });
  }

  var th = document.getElementById('theme');
  if (th) th.addEventListener('click', function () {
    var dark = root.dataset.theme ? root.dataset.theme === 'dark'
      : window.matchMedia('(prefers-color-scheme: dark)').matches;
    root.dataset.theme = dark ? 'light' : 'dark';
    state.theme = root.dataset.theme; save();
  });

  // Read aloud: each section's button reads that section with the device's voice.
  var synth = window.speechSynthesis;
  var buttons = document.querySelectorAll('.read');
  if (!synth) { buttons.forEach(function (b) { b.hidden = true; }); return; }
  var lang = body.dataset.voice, current = null;
  function label(b, on) {
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
    b.lastChild.textContent = ' ' + (on ? body.dataset.stop : body.dataset.read);
  }
  function stop() { synth.cancel(); if (current) label(current, false); current = null; }
  function pickVoice() {
    var vs = synth.getVoices(), base = lang.split('-')[0];
    return vs.filter(function (v) { return v.lang === lang; })[0]
      || vs.filter(function (v) { return v.lang.indexOf(base) === 0; })[0] || null;
  }
  buttons.forEach(function (b) {
    label(b, false);
    b.addEventListener('click', function () {
      if (current === b) { stop(); return; }
      stop();
      var sec = b.closest('section');
      var clone = sec.cloneNode(true);
      clone.querySelectorAll('.read').forEach(function (x) { x.remove(); });
      clone.querySelectorAll('h2,h3,p,li,dt,dd,th,td').forEach(function (x) { x.append('. '); });
      var u = new SpeechSynthesisUtterance(clone.textContent.replace(/\s+/g, ' ').replace(/(\.\s*){2,}/g, '. '));
      u.lang = lang; var v = pickVoice(); if (v) u.voice = v;
      u.rate = 0.9;
      u.onend = u.onerror = function () { if (current === b) stop(); };
      current = b; label(b, true);
      synth.speak(u);
    });
  });
})();
