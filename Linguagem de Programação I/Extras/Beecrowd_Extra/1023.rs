use std::io::{self, BufRead};
use std::collections::BTreeMap;

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let mut T = 0;
    loop {
        let line = lines.next().unwrap().unwrap();
        let N: i32 = line.trim().parse().unwrap();
        if N == 0 {
            break;
        }

        if T > 0 {
            println!();
        }

        let mut totalX = 0;
        let mut totalY = 0;
        let mut consumos = BTreeMap::new();
        for _ in 0..N {
            let line = lines.next().unwrap().unwrap();
            let inputs: Vec<i32> = line.split_whitespace().map(|x| x.parse().unwrap()).collect();
            let (X, Y) = (inputs[0], inputs[1]);
            totalX += X;
            totalY += Y;
            let key = Y / X;
            *consumos.entry(key).or_insert(0) += X;
        }

        T += 1;
        println!("Cidade# {}:", T);

        let mut output = Vec::new();
        for (key, value) in &consumos {
            output.push(format!("{}-{}", value, key));
        }

        println!("{}", output.join(" "));

        let consumo_medio = ((100.0 * totalY as f64) / totalX as f64).floor() / 100.0;
        println!("Consumo medio: {:.2} m3.", consumo_medio);
    }
}