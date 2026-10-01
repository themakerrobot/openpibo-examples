// 문서 페이지 상단 버전 바: 기기·버전 전환, 테스트 중·구버전 안내
(function () {
  var s = document.currentScript;
  var cfg = window.DOCS_VERSIONS;
  if (!s || !cfg) return;
  var root = s.dataset.root, dev = s.dataset.device, tag = s.dataset.tag, page = s.dataset.page;
  var lang = s.dataset.lang === 'en' ? 'en' : 'ko';
  var EN = lang === 'en';
  var LABEL = EN
    ? { released: 'release', testing: 'testing', legacy: 'legacy' }
    : { released: '배포', testing: '테스트 중', legacy: '구버전' };

  function find(d, t) {
    var x = cfg.devices.filter(function (y) { return y.id === d; })[0];
    return x && x.versions.filter(function (v) { return v.tag === t; })[0];
  }
  // 영문(en/)이 없는 버전으로 가면 한국어로
  function langOf(d, t, l) {
    var v = find(d, t);
    return l === 'en' && v && (v.langs || []).indexOf('en') >= 0 ? 'en' : 'ko';
  }
  function url(d, t, p, l) {
    return root + d + '/' + t + '/' + (langOf(d, t, l) === 'en' ? 'en/' : '') + (p || 'index.html');
  }

  // 같은 페이지가 대상 버전(언어)에 있으면 그 페이지로, 없으면 대상 첫 화면으로
  function go(d, t, l) {
    l = l || lang;
    var target = url(d, t, page, l);
    fetch(target, { method: 'HEAD' })
      .then(function (r) { location.href = r.ok ? target : url(d, t, '', l); })
      .catch(function () { location.href = target; });
  }

  var device = cfg.devices.filter(function (x) { return x.id === dev; })[0];
  if (!device) return;
  var cur = device.versions.filter(function (v) { return v.tag === tag; })[0] || {};

  var bar = document.createElement('div');
  bar.className = 'vbar';

  var home = document.createElement('a');
  home.className = 'vbar-home';
  home.href = root + 'index.html';
  home.title = EN ? 'Docs by version' : '버전별 문서 목록';
  home.setAttribute('aria-label', EN ? 'OpenPibo Guide — docs by version' : 'OpenPibo 가이드 — 버전별 문서 목록');
  home.innerHTML = '<span class="mark" aria-hidden="true">P</span><span class="label">' + (EN ? 'OpenPibo Guide' : 'OpenPibo 가이드') + '</span>';
  bar.appendChild(home);

  var devs = document.createElement('span');
  devs.className = 'vbar-devices';
  cfg.devices.forEach(function (d) {
    var a = document.createElement('a');
    a.textContent = d.name;
    a.href = '#';
    if (d.id === dev) a.className = 'on';
    a.onclick = function (e) {
      e.preventDefault();
      if (d.id === dev) return;
      var same = d.versions.filter(function (v) { return v.tag === tag; })[0];
      var rel = d.versions.filter(function (v) { return v.status === 'released'; })[0];
      go(d.id, (same || rel || d.versions[0]).tag);
    };
    devs.appendChild(a);
  });
  bar.appendChild(devs);

  var sel = document.createElement('select');
  sel.setAttribute('aria-label', EN ? 'Version' : '버전');
  device.versions.forEach(function (v) {
    var o = document.createElement('option');
    o.value = v.tag;
    o.textContent = v.tag + ' · ' + (LABEL[v.status] || v.status);
    if (v.tag === tag) o.selected = true;
    sel.appendChild(o);
  });
  sel.onchange = function () { go(dev, sel.value); };
  bar.appendChild(sel);

  // 한국어 / English (영문 문서가 있는 버전만)
  if ((cur.langs || []).indexOf('en') >= 0) {
    var langs = document.createElement('span');
    langs.className = 'vbar-devices vbar-langs';
    [['ko', '한국어'], ['en', 'English']].forEach(function (x) {
      var a = document.createElement('a');
      a.textContent = x[1];
      a.lang = x[0];
      a.href = '#';
      if (x[0] === lang) a.className = 'on';
      a.onclick = function (e) {
        e.preventDefault();
        if (x[0] !== lang) go(dev, tag, x[0]);
      };
      langs.appendChild(a);
    });
    bar.appendChild(langs);
  }

  // 이 버전의 예제 폴더(GitHub)가 있으면 링크
  if (cur.examples) {
    var ex = document.createElement('a');
    ex.className = 'vbar-examples';
    ex.href = cur.examples;
    ex.target = '_blank';
    ex.rel = 'noopener';
    ex.textContent = EN ? 'Examples' : '예제';
    ex.title = EN ? 'Examples for this version (GitHub)' : '이 버전의 예제 (GitHub)';
    bar.appendChild(ex);
  }

  document.body.insertBefore(bar, document.body.firstChild);
  document.documentElement.classList.add('has-vbar');

  if (cur.status === 'testing') {
    var warn = document.createElement('div');
    warn.className = 'vbar-warn';
    warn.textContent = EN
      ? 'Test version (' + tag + '), not yet officially released. Content may change.'
      : '테스트 중인 버전(' + tag + ')입니다. 공식 배포 전이라 내용이 바뀔 수 있습니다.';
    bar.appendChild(warn);
  } else if (cur.status === 'legacy') {
    var old = document.createElement('div');
    old.className = 'vbar-warn';
    old.textContent = EN
      ? 'Legacy docs (' + tag + '). Only for devices running an OS older than 260624v1.'
      : '구버전(' + tag + ') 문서입니다. 260624v1 이전 OS를 쓰는 기기에서만 보세요.';
    bar.appendChild(old);
  }

  // 바 높이만큼 본문·사이드바를 내린다 (화면 폭에 따라 줄바꿈되므로 실제 높이를 잰다)
  function fit() { document.documentElement.style.setProperty('--vbar-total', bar.offsetHeight + 'px'); }
  fit();
  window.addEventListener('resize', fit);
})();
