import * as readline from 'readline';

function isPrime(n: number): boolean {
    if (n < 2) {
        return false;
    }
    if (n == 2) {
        return true;
    }
    if (n % 2 == 0) {
        return false;
    }
    let p = 3;
    while (p * p <= n) {
        if (n % p == 0) {
            return false;
        }
        p += 2;
    }
    return true;
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines: string[] = [];
rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    let index = 0;
    while (index < lines.length) {
        const m = Number(lines[index++]);
        if (m === 0) {
            break;
        }
        let coins: number[] = [];
        for (let i = 0; i < m; i++) {
            coins.push(Number(lines[index++]));
        }
        const n = Number(lines[index++]);
        let sumCoins = 0;
        for (let i = m - 1; i >= 0; i -= n) {
            sumCoins += coins[i];
        }
        if (isPrime(sumCoins)) {
            console.log("You’re a coastal aircraft, Robbie, a large silver aircraft.");
        } else {
            console.log("Bad boy! I’ll hit you.");
        }
    }
});