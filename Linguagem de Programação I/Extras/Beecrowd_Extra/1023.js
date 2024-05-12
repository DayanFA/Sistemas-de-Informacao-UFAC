const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let T = 0;
let input = [];

readline.on('line', (line) => {
    input.push(line);
});

readline.on('close', () => {
    for (let i = 0; i < input.length; i++) {
        let N = parseInt(input[i]);
        if (N === 0) break;

        if (T > 0) console.log();

        let totalX = 0, totalY = 0;
        let consumos = [];
        for (let j = 0; j < N; j++) {
            let [X, Y] = input[++i].split(' ').map(Number);
            totalX += X;
            totalY += Y;
            let key = Math.floor(Y / X);
            let found = false;
            for (let pair of consumos) {
                if (pair.key === key) {
                    pair.value += X;
                    found = true;
                    break;
                }
            }
            if (!found) {
                consumos.push({ key, value: X });
            }
        }

        T++;
        console.log(`Cidade# ${T}:`);

        consumos.sort((a, b) => a.key - b.key);
        for (let pair of consumos) {
            console.log(`${pair.value}-${pair.key} `);
        }

        let consumo_medio = Math.floor((100.0 * totalY) / totalX) / 100;
        console.log(`Consumo medio: ${consumo_medio.toFixed(2)} m3.`);
    }
});