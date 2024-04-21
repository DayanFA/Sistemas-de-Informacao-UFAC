function is_prime(n) {
    if (n < 2) {
        return false;
    }
    if (n === 2) {
        return true;
    }
    if (n % 2 === 0) {
        return false;
    }
    let p = 3;
    while (p * p <= n) {
        if (n % p === 0) {
            return false;
        }
        p += 2;
    }
    return true;
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

readline.on('line', (line) => {
    input.push(line);
}).on('close', () => {
    let i = 0;
    while (i < input.length) {
        let M = Number(input[i++]);
        let coins = [];
        for (let j = 0; j < M; j++) {
            coins.push(Number(input[i++]));
        }
        let N = Number(input[i++]);
        let sum_coins = 0;
        for (let j = M - 1; j >= 0; j -= N) {
            sum_coins += coins[j];
        }
        if (is_prime(sum_coins)) {
            console.log("You’re a coastal aircraft, Robbie, a large silver aircraft.");
        } else {
            console.log("Bad boy! I’ll hit you.");
        }
    }
});