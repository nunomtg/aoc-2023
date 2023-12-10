use std::time::Instant;
use std::{fs, vec};
use std::cmp::Ordering;
use std::collections::HashMap;

fn get_card_rank(card: &Vec<char>) -> i32 {
    let mut letter_counts: HashMap<char,i32> = HashMap::new();

    for c in card {
        *letter_counts.entry(*c).or_insert(0) += 1;
    }
    let mut most_common = 0;
    for count in letter_counts.values() {
        if count > &most_common {
            most_common = *count;
        }
    } 

    match (letter_counts.len(), most_common) {
        (1, _) => return 6,
        (2, 4) => return 5,
        (2, _) => return 4,
        (3, 3) => return 3,
        (3, _) => return 2,
        (4, _) => return 1,
        (_, _) => return 0,
    }
}
struct CHand {
    card: Vec<char>,
    rank: i32,
    bid: i32,
}

impl Eq for CHand {}

impl PartialEq for CHand {
    fn eq(&self, other: &Self) -> bool {
        if self.rank != other.rank {
            return false;
        }

        // Then, check if all cards are equal
        for i in 0..6 {
            if self.card[i] != other.card[i] {
                return false;
            }
        }

        // If all checks passed, the hands are equal
        true
    }
}


impl PartialOrd for CHand {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        if self.rank == other.rank {
            for i in 0..6 {
                if self.card[i] != other.card[i] {
                    return self.card[i].partial_cmp(&other.card[i]);
                }
            }
        }
        return self.rank.partial_cmp(&other.rank);
    }
}

impl Ord for CHand {
    fn cmp(&self, other: &Self) -> Ordering {
        if self.rank == other.rank {
            for i in 0..6 {
                if self.card[i] != other.card[i] {
                    return self.card[i].cmp(&other.card[i]);
                }
            }
        }
        return self.rank.cmp(&other.rank);
    }
}




fn main() {
    let start_time = Instant::now();
    //////////////////////////////////////////////////////////////////////////////////
    let lines = fs::read_to_string("src/input.txt").expect("Error reading input.txt");
    let mut lines: std::str::Lines<'_> = lines.lines();

    let mut all_hands: Vec<CHand> = Vec::new();

    for line in lines {
        let mut line = line.split_ascii_whitespace();
        let hand = line.next().unwrap().chars().collect::<Vec<char>>();
        let bid = line.next().unwrap().parse::<i32>().unwrap();
        let rank = get_card_rank(&hand);
        let new_hand = CHand {
            card: hand,
            rank: rank,
            bid: bid,
        };
        all_hands.push(new_hand);
    }
    // card_score = {c: i for i, c in enumerate("23456789TJQKA")

    static CARD_SCORE_1: HashMap<char, i32> = HashMap::from([
        ('2', 0),
        ('3', 1),
        ('4', 2),
        ('5', 3),
        ('6', 4),
        ('7', 5),
        ('8', 6),
        ('9', 7),
        ('T', 8),
        ('J', 9),
        ('Q', 10),
        ('K', 11),
        ('A', 12),
    ]);
    let mut card_score: HashMap<char, i32> = HashMap::new();
    let mut i = 0;
    for c in "23456789TJQKA".chars() {
        card_score.insert(c, i);
        i += 1;
    }
    // print all_hands
    all_hands.sort();
    for hand in all_hands {
        println!("{} {} {}", hand.card.iter().collect::<String>(), hand.rank, hand.bid);
    }


    // println!("Part 1: {}", part1);
    // println!("Part 2: {}", part2);
    //////////////////////////////////////////////////////////////////////////////////
    let end_time = Instant::now();
    let duration = end_time.duration_since(start_time).as_micros() as f64 / 1000.0;

    println!("Rust program executed in {:?} ms", duration);
}
