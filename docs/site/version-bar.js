// 문서 페이지 상단 버전 바: 기기·버전 전환, 테스트 중 버전 안내
(function () {
  var s = document.currentScript;
  var cfg = window.DOCS_VERSIONS;
  if (!s || !cfg) return;
  var root = s.dataset.root, dev = s.dataset.device, tag = s.dataset.tag, page = s.dataset.page;
  var LABEL = { released: '배포', testing: '테스트 중' };

  function url(d, t, p) { return root + d + '/' + t + '/' + (p || 'index.html'); }

  // 같은 페이지가 대상 버전에 있으면 그 페이지로, 없으면 대상 버전 첫 화면으로
  function go(d, t) {
    var target = url(d, t, page);
    fetch(target, { method: 'HEAD' })
      .then(function (r) { location.href = r.ok ? target : url(d, t); })
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
  home.title = '버전별 문서 목록';
  home.setAttribute('aria-label', 'OpenPibo 가이드 — 버전별 문서 목록');
  home.innerHTML = '<span class="mark" aria-hidden="true">P</span><span class="label">OpenPibo 가이드</span>';
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
  sel.setAttribute('aria-label', '버전');
  device.versions.forEach(function (v) {
    var o = document.createElement('option');
    o.value = v.tag;
    o.textContent = v.tag + ' · ' + (LABEL[v.status] || v.status);
    if (v.tag === tag) o.selected = true;
    sel.appendChild(o);
  });
  sel.onchange = function () { go(dev, sel.value); };
  bar.appendChild(sel);

  document.body.insertBefore(bar, document.body.firstChild);
  document.documentElement.classList.add('has-vbar');

  if (cur.status === 'testing') {
    var warn = document.createElement('div');
    warn.className = 'vbar-warn';
    warn.textContent = '테스트 중인 버전(' + tag + ')입니다. 공식 배포 전이라 내용이 바뀔 수 있습니다.';
    bar.appendChild(warn);
  }

  // 바 높이만큼 본문·사이드바를 내린다 (화면 폭에 따라 줄바꿈되므로 실제 높이를 잰다)
  function fit() { document.documentElement.style.setProperty('--vbar-total', bar.offsetHeight + 'px'); }
  fit();
  window.addEventListener('resize', fit);
})();
