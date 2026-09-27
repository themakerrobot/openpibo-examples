// openpibo-os IDE의 블록 정의(customblock.js)와 파이썬 생성기(customblock_callback.js)를 읽어
// { type: { fields: {name: [허용값...] | null}, inputs: [...], generator: bool } } JSON 을 출력한다.
// 사용: node extract_blocks.js <openpibo-os>/ide/static
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const dir = process.argv[2];
const defs = {};
const gens = new Set();

const anyProxy = () => new Proxy(function () {}, {
  get: (t, k) => (k === Symbol.toPrimitive ? () => '' : anyProxy()),
  apply: () => anyProxy(),
  construct: () => anyProxy(),
  set: () => true,
});

const forBlock = new Proxy({}, { set: (t, k) => { gens.add(k); return true; } });
const Blockly = new Proxy({
  defineBlocksWithJsonArray: (arr) => arr.forEach((b) => { defs[b.type] = b; }),
  Blocks: new Proxy({}, { set: (t, k) => { defs[k] = defs[k] || { type: k }; return true; } }),
  Python: new Proxy({ forBlock }, {
    get: (t, k) => (k === 'forBlock' ? forBlock : anyProxy()),
    set: (t, k) => { gens.add(k); return true; },
  }),
}, { get: (t, k) => (k in t ? t[k] : anyProxy()) });

const ctx = vm.createContext(new Proxy({ Blockly, console, JSON, Object, Array, String, Number, Math, parseInt, parseFloat }, {
  has: () => true,
  get: (t, k) => (k in t ? t[k] : (k === Symbol.unscopables ? undefined : anyProxy())),
}));
for (const f of ['customblock.js', 'customblock_callback.js']) {
  try { vm.runInContext(fs.readFileSync(path.join(dir, f), 'utf8'), ctx, { filename: f }); }
  catch (e) { console.error(`[warn] ${f}: ${e.message}`); }
}

// Blockly 기본 블록 (logic_, math_ 등): blocks_compressed.js 에 정의된 타입 이름
const core = fs.readFileSync(path.join(dir, 'blocks_compressed.js'), 'utf8');
const coreTypes = new Set([...core.matchAll(/type:"([a-zA-Z_0-9]+)"/g)].map((m) => m[1]));
// Blocks["x"] 로 직접 정의된 기본 블록도 포함
[...core.matchAll(/blocks\$[a-z]+\.([a-zA-Z_0-9]+)=/g)].forEach((m) => coreTypes.add(m[1]));

const out = {};
for (const [type, d] of Object.entries(defs)) {
  const fields = {}; const inputs = [];
  for (let i = 0; i < 10; i++) {
    for (const a of d['args' + i] || []) {
      if (!a || !a.name) continue;
      if (a.type && a.type.startsWith('input_')) inputs.push(a.name);
      else if (a.type === 'field_dropdown' && Array.isArray(a.options)) {
        const vals = a.options.map((o) => o[1]);
        // 파일 목록처럼 런타임에 채워지는 드롭다운은 검사하지 않는다
        fields[a.name] = vals.length <= 1 ? null : vals;
      } else fields[a.name] = null;
    }
  }
  out[type] = { fields, inputs, generator: gens.has(type) };
}
for (const t of coreTypes) if (!out[t]) out[t] = { core: true, generator: true };
process.stdout.write(JSON.stringify(out));
