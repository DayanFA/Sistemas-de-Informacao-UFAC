use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let t: i32 = lines.next().unwrap().unwrap().parse().unwrap();
    for i in 1..=t {
        let correct = lines.next().unwrap().unwrap();
        let team1 = lines.next().unwrap().unwrap();
        let team2 = lines.next().unwrap().unwrap();

        let mut score1 = 0;
        let mut score2 = 0;
        for (c, (t1, t2)) in correct.chars().zip(team1.chars().zip(team2.chars())) {
            if c == t1 {
                score1 += 1;
            }
            if c == t2 {
                score2 += 1;
            }
        }

        println!("Instancia {}", i);
        if score1 > score2 {
            println!("time 1");
        } else if score1 < score2 {
            println!("time 2");
        } else {
            let mut tie_breaker = false;
            for (c, (t1, t2)) in correct.chars().zip(team1.chars().zip(team2.chars())) {
                if c == t1 && c != t2 {
                    println!("time 1");
                    tie_breaker = true;
                    break;
                } else if c != t1 && c == t2 {
                    println!("time 2");
                    tie_breaker = true;
                    break;
                }
            }
            if !tie_breaker {
                println!("empate");
            }
        }
        println!();
    }
}