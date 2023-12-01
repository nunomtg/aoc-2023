use std::fs;
use std::collections::HashMap;

fn main() {
    #[allow(non_snake_case)]
    let NUMS: HashMap<&str, u32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ("9", 9),
        ]);

    let contents = fs::read_to_string("src/input.txt")
        .expect("Something went wrong reading the file");
    
    let lines: Vec<&str> = contents.split("\n").collect();
    #[allow(unused_variables)]
    let mut sum1: u32 = 0;
    #[allow(unused_variables)]
    let mut sum2: u32 = 0;

    for line in lines.iter() {
        let mut v1: Vec<u32> = Vec::new();
        let mut v2: Vec<u32> = Vec::new();
        for i in 0..line.len() {
            let new_line: String = line.chars().skip(i).collect();
            for (key, value) in NUMS.iter() {
                if new_line.starts_with(key) {
                    if key != &"one" && key != &"two" && key != &"three" && key != &"four" && key != &"five" && key != &"six" && key != &"seven" && key != &"eight" && key != &"nine" {
                        v1.push(*value);
                    } 
                    v2.push(*value);
                }
            }
        }
        sum1 += v1.first().unwrap() * 10 + v1.last().unwrap();
        sum2 += v2.first().unwrap() * 10 + v2.last().unwrap();
    }

    // println!("Part 1: {}", sum1);
    // println!("Part 2: {}", sum2);
}