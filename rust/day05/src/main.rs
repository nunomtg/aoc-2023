use std::time::Instant;
use std::{fs, vec};
use std::collections::VecDeque;

// Create function that receives a tuple u32, u32 and returns a tuple of a tuple u32, u32 and vec of tuple u32, u32
fn get_next((x1,x2): (i64, i64), (y1, y2): (i64, i64), delta: i64) -> ((i64, i64), Vec<(i64, i64)>) {
    if y2 < x1 || x2 < y1 {
        return ((-1,-1), vec![]);
    }
    let new_x1 = x1.max(y1) + delta;
    let new_x2 = x2.min(y2) + delta;
    let mut to_change: Vec<(i64,i64)> = vec![];
    for (start, end) in vec![(x1, y1 - 1), (y2 + 1, x2)] {
        if start < end {
            to_change.push((start, end));
        }
    }
    return ((new_x1, new_x2), to_change);
}

fn solve_for_init_range(mut ranges:Vec<(i64,i64)>, lines: std::str::Lines<'_>) -> i64 {
    let mut q = VecDeque::new();
    let mut rules: Vec<(i64, i64, i64)> = vec![];
    let mut new_ranges: Vec<(i64, i64)>  = vec![];
    for line in lines {
        if line.ends_with(':') {
            rules = vec![];
            new_ranges = vec![];
            q = VecDeque::from(ranges.clone());
        }
        else if line.is_empty() {
            while !q.is_empty() {
                let r = q.pop_front().unwrap();
                let mut changed = false;
                for rule in rules.iter() {
                    match get_next(r, (rule.0, rule.1), rule.2) {
                        ((-1,-1), _) => continue,
                        ((x1,x2), new) => {
                            if new.len() > 0 {
                                q.extend(new);
                            }
                            new_ranges.push((x1,x2));
                            changed = true;
                            break
                        }
                    }
                }
                if changed == false {
                    new_ranges.push(r);
                }
            }
            ranges = new_ranges.clone();
            
        }
        else {
            let tmp = line.split_ascii_whitespace()
                                    .map(|x| x.parse::<i64>().unwrap())
                                    .collect::<Vec<i64>>();
            rules.push((tmp[1], tmp[1] + tmp[2] - 1, tmp[0] - tmp[1]));
        }
    }
    return ranges.into_iter().map(|(x,_y)| x).min().unwrap();
}

fn main() {
    let start_time = Instant::now();
    //////////////////////////////////////////////////////////////////////////////////
    let lines = fs::read_to_string("src/input.txt").expect("Error reading input.txt");
    let mut lines: std::str::Lines<'_> = lines.lines();

    let initial_ranges = lines.nth(0)
                                        .unwrap()
                                        .split(": ")
                                        .nth(1)
                                        .unwrap()
                                        .split_ascii_whitespace()
                                        .map(|x| x.parse::<i64>().unwrap())
                                        .collect::<Vec<i64>>();
    lines.nth(0);

    let part1_range = initial_ranges.iter()
                                                    .map(|x| (*x,*x))
                                                    .collect::<Vec<(i64,i64)>>();

    let part2_range = initial_ranges.chunks(2)
                                                    .map(|x| (x[0], x[0] + x[1] - 1))
                                                    .collect::<Vec<(i64,i64)>>();
    
    #[allow(unused_variables)]
    let part1 = solve_for_init_range(part1_range, lines.clone());
    #[allow(unused_variables)]
    let part2 = solve_for_init_range(part2_range, lines);
    // println!("Part 1: {}", part1);
    // println!("Part 2: {}", part2);
    //////////////////////////////////////////////////////////////////////////////////
    let end_time = Instant::now();
    let duration = end_time.duration_since(start_time).as_micros() as f64 / 1000.0;

    println!("Rust program executed in {:?} ms", duration);
}
