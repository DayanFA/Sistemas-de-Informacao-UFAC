import * as readline from 'readline';

let rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('', (input: string) => {
    let times: number[] = input.split(' ').map(Number);
    let [sh, sm, eh, em] = times;

    let st = sh * 60 + sm;
    let et = eh * 60 + em;
    let d = et - st;
    if (d <= 0) {
        d += 24 * 60;
    }
    let h = Math.floor(d / 60);
    let m = d % 60;
    console.log(`O JOGO DUROU ${h} HORA(S) E ${m} MINUTO(S)`);
    rl.close();
});