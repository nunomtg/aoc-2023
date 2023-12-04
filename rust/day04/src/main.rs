use std::time::Instant;
use std::fs;
use std::collections::{HashSet, VecDeque};

fn main() {
    let start_time = Instant::now();
    //////////////////////////////////////////////////////////////////////////////////
    let lines = fs::read_to_string("src/input.txt").expect("Error reading input.txt");
    let lines = lines.lines();

    let mut scores: Vec<u32> = Vec::new();

    for card in lines {
        let mut split_card =  card.split([':', '|']);
        let ll = split_card.nth(1).unwrap().split_ascii_whitespace().collect::<HashSet<&str>>();
        let rr = split_card.last().unwrap().split_ascii_whitespace().collect::<HashSet<&str>>();

        let intersec_len: HashSet<_> = ll.intersection(&rr).collect();
        scores.push(intersec_len.len() as u32);
    }
    #[allow(unused_variables)]
    let score_1 = scores.iter().map(|x| if x > &0 {(2 as u32).pow(x-1)} else {0}).sum::<u32>();
    #[allow(unused_variables)]
    let mut score_2 = 0;
    let mut q = (0..scores.len()).collect::<VecDeque<usize>>();

    while !q.is_empty() {
        score_2 += 1;
        let curr_card = q.pop_front().unwrap();
        q.extend(curr_card+1..curr_card+scores[curr_card] as usize+1)
    }


    // println!("Part 1: {}", score_1);
    // println!("Part 2: {}", score_2);
    //////////////////////////////////////////////////////////////////////////////////
    let end_time = Instant::now();
    let duration = end_time.duration_since(start_time).as_micros() as f64 / 1000.0;

    println!("Rust program executed in {:?} ms", duration);
}
