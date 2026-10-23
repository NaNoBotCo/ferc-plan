(function () {
  var root = document.documentElement;
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

  // Floating "Choose" button: hidden while the Choose section is on screen.
  var fl = document.getElementById('float'), ch = document.getElementById('choose');
  if (fl && ch && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (es) {
      fl.classList.toggle('hide', es[0].isIntersecting);
    }, { threshold: 0 }).observe(ch);
  }
})();

// Read aloud: one line at a time; the line being read is marked and scrolled into view.
(function () {
  var body = document.body, synth = window.speechSynthesis;
  var buttons = document.querySelectorAll('.read');
  if (!synth || !window.SpeechSynthesisUtterance) { buttons.forEach(function (b) { b.hidden = true; }); return; }
  var lang = body.dataset.voice, current = null, queue = [], marked = null, run = 0;
  var SEL = 'h1,h2,h3,h4,legend,p,li,dt,dd,th,td,summary,label.pick,.opt';
  function label(b, on) {
    b.setAttribute('aria-pressed', on ? 'true' : 'false');
    b.lastChild.textContent = ' ' + (on ? body.dataset.stop : body.dataset.read);
  }
  function unmark() { if (marked) marked.classList.remove('speaking'); marked = null; }
  function stop() { run++; queue = []; synth.cancel(); unmark(); if (current) label(current, false); current = null; }
  function voice() {
    var vs = synth.getVoices(), base = lang.split('-')[0];
    return vs.filter(function (v) { return v.lang === lang && v.localService; })[0]
      || vs.filter(function (v) { return v.lang.indexOf(base) === 0 && v.localService; })[0]
      || vs.filter(function (v) { return v.lang.indexOf(base) === 0; })[0] || null;
  }
  function textOf(el) {
    var c = el.cloneNode(true);
    c.querySelectorAll('[aria-hidden="true"],.read,.vh,input,textarea,select').forEach(function (x) { x.remove(); });
    return c.textContent.replace(/\s+/g, ' ').trim();
  }
  function hidden(el) {
    if (el.closest('[hidden]')) return true;
    var d = el.closest('details');
    return !!d && !d.open && !el.closest('summary');
  }
  function blocks(scope) {
    if (scope.id === 'choose') {
      var pv = document.getElementById('pv');
      if (pv) return [{ el: pv.parentNode, text: pv.textContent }];
    }
    var all = Array.prototype.slice.call(scope.querySelectorAll(SEL)).filter(function (el) {
      return !hidden(el) && !el.closest('.read');
    });
    // keep only the innermost blocks, so nothing is read twice
    return all.filter(function (el) {
      return !all.some(function (o) { return o !== el && el.contains(o); });
    }).map(function (el) { return { el: el, text: textOf(el) }; })
      .filter(function (b) { return b.text; });
  }
  function next() {
    unmark();
    var b = queue.shift();
    if (!b) { stop(); return; }
    marked = b.el; marked.classList.add('speaking');
    try { marked.scrollIntoView({ block: 'center', behavior: 'smooth' }); } catch (_) { marked.scrollIntoView(); }
    var u = new SpeechSynthesisUtterance(b.text);
    u.lang = lang; var v = voice(); if (v) u.voice = v;
    u.rate = 0.9;
    var mine = run;
    u.onend = u.onerror = function () { if (current && mine === run) next(); };
    synth.speak(u);
  }
  buttons.forEach(function (b) {
    label(b, false);
    b.addEventListener('click', function () {
      if (current === b) { stop(); return; }
      stop();
      var scope = b.closest('li.step') || b.closest('section') || document.body;
      queue = blocks(scope);
      current = b; label(b, true);
      next();
    });
  });
})();

// Choose and send: ticks and answers build one message to NaN, sent from the reader's own email.
(function () {
  var form = document.getElementById('chooser');
  if (!form) return;
  var c = JSON.parse(form.dataset.cfg);
  var send = document.getElementById('send'), total = document.getElementById('total');
  var pv = document.getElementById('pv'), copied = document.getElementById('copied');
  var fmt = function (n) {
    var t = n.toLocaleString('en-US');
    return c.de ? t.replace(/,/g, '’') + ' Baht' : '฿' + t;
  };
  function all(name) {
    return Array.prototype.filter.call(form.elements, function (x) { return x.name === name; });
  }
  function picked(name) {
    return all(name).filter(function (x) { return x.checked; });
  }
  function webRule() {
    var wp = picked('web').some(function (x) { return x.value === '3A'; });
    all('extra').forEach(function (x) {
      if (x.dataset.needs !== '3A') return;
      x.disabled = !wp;
      if (!wp) x.checked = false;
      x.closest('label').classList.toggle('off', !wp);
    });
  }
  function build() {
    webRule();
    var once = 0, month = 0;
    picked('extra').forEach(function (x) { once += +x.dataset.once; month += +x.dataset.month; });
    function both(o, m) {
      var parts = [];
      if (o) parts.push(fmt(o) + ' ' + c.once);
      if (m) parts.push(fmt(m) + ' ' + c.month);
      return parts.join(' ' + c.and + ' ');
    }
    var half = picked('pay').some(function (x) { return x.value === c.half; });
    var sum = once || month;
    var sumText = c.total + ': ' + (sum ? both(once, month) : c.none);
    if (sum && half) sumText += '. ' + c.money + ': ' + both(once / 2, month / 2);
    total.textContent = sumText;
    var lines = [c.head, ''];
    function block(title, items) {
      if (!items.length) return;
      lines.push(title + ':');
      items.forEach(function (t) { lines.push('- ' + t); });
      lines.push('');
    }
    block(c.plan, picked('step').map(function (x) { return x.dataset.label; }));
    block(c.web, picked('web').map(function (x) { return x.dataset.label; }));
    block(c.extras, picked('extra').map(function (x) { return x.dataset.label; }));
    if (sum) {
      lines.push(sumText); lines.push('');
      block(c.pay, picked('pay').map(function (x) { return x.value; }));
    }
    block(c.trade, picked('trade').map(function (x) { return x.dataset.label; }));
    var ans = [];
    form.querySelectorAll('fieldset.q').forEach(function (fs) {
      var k = fs.dataset.q;
      var a = picked('q-' + k).map(function (x) { return x.value; });
      var note = all('qn-' + k).map(function (x) { return x.value.trim(); }).filter(Boolean);
      if (a.length || note.length) ans.push(fs.dataset.text + ' ' + a.concat(note).join('; '));
    });
    block(c.answers, ans);
    var g = form.elements.groups.value.trim();
    if (g) block(c.groups, [g]);
    var n = form.elements.name.value.trim();
    if (n) lines.push(n);
    var text = lines.join('\n').trim();
    pv.textContent = text;
    send.href = 'mailto:' + c.to + '?subject=' + encodeURIComponent(c.subject) + '&body=' + encodeURIComponent(text);
    return text;
  }
  function changed() { copied.textContent = ''; build(); }
  form.addEventListener('change', changed);
  form.addEventListener('input', changed);
  form.addEventListener('submit', function (ev) { ev.preventDefault(); });
  build();
  document.getElementById('copy').addEventListener('click', function () {
    var text = build();
    function done() { copied.textContent = c.copied; }
    if (navigator.clipboard) navigator.clipboard.writeText(text).then(done, function () { copied.textContent = text; });
    else copied.textContent = text;
  });
})();
