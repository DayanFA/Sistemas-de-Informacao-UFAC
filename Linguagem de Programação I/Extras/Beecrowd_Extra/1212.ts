import * as readline from 'readline';

let rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input: string[] = [];

rl.on('line', (line) => {
    input.push(line);
});

rl.on('close', () => {
    for (let i = 0; i < input.length; i++) {
        let a: string[] = input[i].split(' ')[0].split('');
        let b: string[] = input[i].split(' ')[1].split('');
        let carry = 0;
        let c = 0;
        if (a.join('') === '0' && b.join('') === '0') {
            break;
        }

        while (a.length < b.length) {
            a.unshift('0');
        }
        while (b.length < a.length) {
            b.unshift('0');
        }

        for (let i = a.length - 1; i >= 0; i--) {
            if ((parseInt(a[i]) + parseInt(b[i]) > 9) || (parseInt(a[i]) + parseInt(b[i]) + c > 9)) {
                carry += 1;
                c = 1;
            } else {
                c = 0;
            }
        }

        if (carry === 0) {
            console.log("No carry operation.");
        } else if (carry === 1) {
            console.log("1 carry operation.");
        } else {
            console.log(carry + " carry operations.");
        }
    }
});