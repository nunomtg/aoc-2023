use std::time::Instant;
use std::fs;

fn sol(t: u64, d:u64) -> u64 {
    let (ll, rr) = (
        0.5 * (t as f32 - ((t.pow(2) - 4 * d) as f32).sqrt()) + 1e-6,
        0.5 * (t as f32 + ((t.pow(2) - 4 * d) as f32).sqrt()) + 1e-6
    );
    let n = (rr.floor() - ll.ceil() + 1.0) as u64;
    return n;
}

fn main() {
    let start_time = Instant::now();
    //////////////////////////////////////////////////////////////////////////////////
    let lines = fs::read_to_string("src/input.txt").expect("Error reading input.txt");
    let mut lines: std::str::Lines<'_> = lines.lines();

    let tt = lines.next().unwrap().split(": ").nth(1).unwrap().split_ascii_whitespace();
    let dd = lines.next().unwrap().split(": ").nth(1).unwrap().split_ascii_whitespace();

    let tt1 = tt.clone().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();
    let dd1 = dd.clone().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();

    let tt2 = tt.collect::<String>().parse::<u64>().unwrap();
    let dd2 = dd.collect::<String>().parse::<u64>().unwrap();

    let iter = tt1.iter().zip(dd1.iter());
    #[allow(unused_variables)]
    let part1 = iter.map(|(t,d)| sol(*t,*d)).reduce(|acc, e| acc * e).unwrap();
    #[allow(unused_variables)]
    let part2 = sol(tt2, dd2);

    // println!("Part 1: {}", part1);
    // println!("Part 2: {}", part2);
    //////////////////////////////////////////////////////////////////////////////////
    let end_time = Instant::now();
    let duration = end_time.duration_since(start_time).as_micros() as f64 / 1000.0;

    println!("Rust program executed in {:?} ms", duration);
}
