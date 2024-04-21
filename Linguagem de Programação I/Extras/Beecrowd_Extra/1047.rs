use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let line = stdin.lock().lines().next().unwrap().unwrap();
    let times: Vec<i32> = line.split_whitespace().map(|s| s.parse().unwrap()).collect();
    let (sh, sm, eh, em) = (times[0], times[1], times[2], times[3]);

    let mut st = sh * 60 + sm;
    let mut et = eh * 60 + em;
    let mut d = et - st;
    if d <= 0 {
        d += 24 * 60;
    }
    let h = d / 60;
    let m = d % 60;
    println!("O JOGO DUROU {} HORA(S) E {} MINUTO(S)", h, m);
}