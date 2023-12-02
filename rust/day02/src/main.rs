use std::fs;
use regex::Regex;
use std::collections::HashMap;
use std::cmp;

fn main() {
    let lines = fs::read_to_string("src/input.txt")
        .expect("Something went wrong reading the file");

    let pat_1 = Regex::new(r"Game ([-+]?\d+):(.+)").unwrap();
    let pat_2 = Regex::new(r" ([-+]?\d+) (.+)").unwrap();

    
    #[allow(unused_variables)]
    let mut score_1: u32 = 0;
    #[allow(unused_variables)]
    let mut score_2: u32 = 0;

    for line in lines.lines() {
        let mut good_game: bool = true;
        let caps = pat_1.captures(line).unwrap();
        let (id, events) = (caps[1].parse::<u32>().unwrap(), &caps[2]);

        let mut master_counter = HashMap::from([(String::from("green"), 0), (String::from("red"), 0), (String::from("blue"), 0)]);
        for event in events.split(";") {
            let mut counter: HashMap<String, u32> = HashMap::from([(String::from("green"), 0), (String::from("red"), 0), (String::from("blue"), 0)]);

            for d in event.split(',') {
                let caps = pat_2.captures(d).unwrap();
                let (num, color) = (caps[1].parse::<u32>().unwrap(), caps[2].to_string());

                counter.entry(color).and_modify(|f| *f += num);
            }

            for (key, value) in counter.iter() {
                master_counter.entry(key.to_string()).and_modify(|f| *f = cmp::max(*f, *value));
            }

            if counter["red"] > 12 || counter["green"] > 13 || counter["blue"] > 14 {
                good_game = false;
            }
        }
        if good_game {
            score_1 += id;
        }

        score_2 += master_counter["red"] * master_counter["green"] * master_counter["blue"];
    }
    // println!("Part 1: {}", score_1);
    // println!("Part 2: {}", score_2);
}
