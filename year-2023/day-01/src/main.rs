extern crate aho_corasick;

use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use aho_corasick::{AhoCorasick};


fn main() -> io::Result<()> {

    let file_path = "/home/hoseoklee/Documents/Programming/advent-of-code/year-2023/day-01/src/calibration_values.txt";
    let file = File::open(&file_path).expect("File read error");
    let reader = BufReader::new(file);

    let result: u32 = reader
        .lines()
        .map(|line| parse_digit(&line.unwrap()))
        .sum();

    println!("{}", result);

    Ok(())
}

fn parse_digit(haystack: &str) -> u32 {

    let patterns = &[
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",

        // Part 2, look for words
        // We use aho_corasick to catch overlapping patterns
        // e.g. sevenine => [7, 9]
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ];

    let ac = AhoCorasick::new(patterns).unwrap();
    let mut matches: Vec<u32> = ac
        .find_overlapping_iter(haystack)
        .map(
            |mat| {
                let index = mat.pattern().as_u32() + 1;

                match index {
                    1..=9 => index,
                    10..=18 => index - 9,
                    _ => panic!("Index overflow")
                }
            }
        )
        .collect();

    matches[0] * 10 + matches[matches.len() - 1]

}
