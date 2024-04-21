use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    loop {
        let line = lines.next().unwrap().unwrap();
        let mut parts = line.split_whitespace();
        let mut a: Vec<char> = parts.next().unwrap().chars().collect();
        let mut b: Vec<char> = parts.next().unwrap().chars().collect();
        let mut carry = 0;
        let mut c = 0;
        if a.iter().collect::<String>() == "0" && b.iter().collect::<String>() == "0" {
            break;
        }

        while a.len() < b.len() {
            a.insert(0, '0');
        }
        while b.len() < a.len() {
            b.insert(0, '0');
        }

        for i in (0..a.len()).rev() {
            if ((a[i].to_digit(10).unwrap() + b[i].to_digit(10).unwrap() > 9) ||
                (a[i].to_digit(10).unwrap() + b[i].to_digit(10).unwrap() + c > 9)) {
                carry += 1;
                c = 1;
            } else {
                c = 0;
            }
        }

        if carry == 0 {
            println!("No carry operation.");
        } else if carry == 1 {
            println!("1 carry operation.");
        } else {
            println!("{} carry operations.", carry);
        }
    }
}