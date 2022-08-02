const fs = require("fs");
let n = parseInt(fs.readFileSync("/dev/stdin").toString().trim());

let d = new Array(n + 1);
d.fill(0);

for (let i = 2; i < n + 1; i++) {
  let a = 1000000;
  let b = 1000000;
  let c = 1000000;

  if (i % 2 === 0) {
    a = d[i / 2] + 1;
  }
  if (i % 3 === 0) {
    b = d[i / 3] + 1;
  }
  c = d[i - 1] + 1;
  d[i] = Math.min(a, b, c);
}
console.log(d[n]);
