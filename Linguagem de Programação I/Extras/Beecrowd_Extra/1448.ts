import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines: string[] = [];
rl.on('line', (line) => {
    lines.push(line);
});

rl.on('close', () => {
    let t = parseInt(lines[0]);
    let index = 1;
    for (let i = 1; i <= t; i++) {
        let correct = lines[index++];
        let team1 = lines[index++];
        let team2 = lines[index++];

        let score1 = 0;
        let score2 = 0;
        for (let j = 0; j < correct.length; j++) {
            if (correct[j] === team1[j]) {
                score1++;
            }
            if (correct[j] === team2[j]) {
                score2++;
            }
        }

        console.log(`Instancia ${i}`);
        if (score1 > score2) {
            console.log("time 1");
        } else if (score1 < score2) {
            console.log("time 2");
        } else {
            let tieBreaker = false;
            for (let j = 0; j < correct.length; j++) {
                if (correct[j] === team1[j] && correct[j] !== team2[j]) {
                    console.log("time 1");
                    tieBreaker = true;
                    break;
                } else if (correct[j] !== team1[j] && correct[j] === team2[j]) {
                    console.log("time 2");
                    tieBreaker = true;
                    break;
                }
            }
            if (!tieBreaker) {
                console.log("empate");
            }
        }
        console.log();
    }
});