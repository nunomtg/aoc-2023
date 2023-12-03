use std::time::Instant;
use std::fs;
use std::collections::HashMap;

// Iterator of tuple (usize, usize)
fn adjacent(row: usize, col: usize, max_row: usize, max_col: usize) -> impl Iterator<Item = (usize, usize)> {
    [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)].iter()
        .filter_map(move |&(dr, dc)| {
            let (new_row, new_col) = (row as isize + dr, col as isize + dc);
            if new_row >= 0 && new_row < max_row as isize && new_col >= 0 && new_col < max_col as isize {
                Some((new_row as usize, new_col as usize))
            } else {
                None
            }
        })
}

fn main() {
    let start_time = Instant::now();
    //////////////////////////////////////////////////////////////////////////////////
    let lines = fs::read_to_string("src/input.txt").expect("Error reading input.txt");
    let lines = lines.lines();

    let matrix = lines.map(|line| line.chars().collect::<Vec<char>>()).collect::<Vec<Vec<char>>>();

    #[allow(non_snake_case)]
    let (MAX_ROW, MAX_COL) = (matrix.len(), matrix[0].len());

    let symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@'];
    #[allow(unused_variables)]
    let mut score_1 = 0;
    let mut gears: HashMap<(usize, usize), Vec<u32>> = HashMap::new();

    for row in 0..MAX_ROW {
        let mut col = 0;
        while col < MAX_COL {
            let mut good = false;
            let mut gear = (MAX_ROW, MAX_COL);
            let mut num: Vec<char> = Vec::new();
            
            while col < MAX_COL && matrix[row][col].is_digit(10) {
                num.push(matrix[row][col]);

                for (r, c) in adjacent(row, col, MAX_ROW, MAX_COL) {
                    if symbols.contains(&matrix[r][c]) {
                        good = true;
                    }
                    if matrix[r][c] == '*' && gear == (MAX_ROW, MAX_COL) {
                        gear = (r, c);
                    }
                }
                col += 1;
            }
            if good {
                let num = num.iter().collect::<String>().parse::<u32>().unwrap();
                score_1 += num;
            }
            if gear != (MAX_ROW, MAX_COL) {
                gears.entry(gear).or_insert(Vec::new()).push(num.iter().collect::<String>().parse::<u32>().unwrap());
            }
            col += 1;
        }
    }
    #[allow(unused_variables)]
    let score_2: u32 = gears.values()
    .filter(|v| v.len() >= 2)
    .map(|v| v.iter().product::<u32>())
    .sum();
    // println!("Part 1: {}", score_1);
    // println!("Part 2: {}", score_2);
    //////////////////////////////////////////////////////////////////////////////////
    let end_time = Instant::now();
    let duration = end_time.duration_since(start_time).as_micros() as f64 / 1000.0;

    println!("Rust program executed in {:?} ms", duration);
}
