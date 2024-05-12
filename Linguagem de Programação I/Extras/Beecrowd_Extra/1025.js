const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];
readline.on('line', line => {
  input.push(line);
});

readline.on('close', () => {
  let T = 1;
  let line = 0;
  while (true) {
    let [N, Q] = input[line++].split(' ').map(Number);
    if (N === 0 && Q === 0) break;

    let marmores = input.slice(line, line + N).map(Number);
    line += N;
    marmores.sort((a, b) => a - b);

    console.log(`CASE# ${T++}:`);

    for (let i = 0; i < Q; ++i) {
      let consulta = Number(input[line++]);

      let index = marmores.indexOf(consulta);

      if (index === -1)
        console.log(`${consulta} not found`);
      else
        console.log(`${consulta} found at ${index + 1}`);
    }
  }
});