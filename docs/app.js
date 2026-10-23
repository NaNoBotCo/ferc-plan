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

// Chooser: ticks build a message to NaN, sent from the reader's own email.
(function () {
  var form = document.getElementById('chooser');
  if (!form) return;
  var c = JSON.parse(form.dataset.cfg);
  var send = document.getElementById('send'), total = document.getElementById('total');
  var fmt = function (n) { return '฿' + n.toLocaleString('en-US'); };
  function picked(name) {
    return Array.prototype.filter.call(form.querySelectorAll('input[name="' + name + '"]'), function (x) { return x.checked; });
  }
  function build() {
    var once = 0, month = 0;
    picked('extra').forEach(function (x) { once += +x.dataset.once; month += +x.dataset.month; });
    var sum = [];
    if (once) sum.push(fmt(once) + ' ' + c.once);
    if (month) sum.push(fmt(month) + ' ' + c.month);
    var sumText = c.total + ': ' + (sum.length ? sum.join(' · ') : c.none);
    total.textContent = sumText;
    var lines = [c.head, ''];
    function block(title, items) {
      if (!items.length) return;
      lines.push(title + ':');
      items.forEach(function (t) { lines.push('- ' + t); });
      lines.push('');
    }
    block(c.plan, picked('step').map(function (x) { return x.dataset.label; }));
    block(c.extras, picked('extra').map(function (x) { return x.dataset.label; }));
    if (sum.length) { lines.push(sumText); lines.push(''); }
    block(c.pay, picked('pay').map(function (x) { return x.value; }));
    block(c.trade, picked('trade').map(function (x) { return x.dataset.label; }));
    var g = form.elements.groups.value.trim();
    if (g) block(c.groups, [g]);
    var n = form.elements.name.value.trim();
    if (n) lines.push(n);
    var text = lines.join('\n').trim();
    send.href = 'mailto:' + c.to + '?subject=' + encodeURIComponent(c.subject) + '&body=' + encodeURIComponent(text);
    return text;
  }
  form.addEventListener('change', build);
  form.addEventListener('input', build);
  build();
  document.getElementById('copy').addEventListener('click', function () {
    var text = build(), out = document.getElementById('copied');
    function done() { out.textContent = c.copied; }
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { out.textContent = text; });
    else out.textContent = text;
  });
})();
