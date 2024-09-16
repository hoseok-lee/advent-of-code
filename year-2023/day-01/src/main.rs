extern crate aho_corasick;

use aho_corasick::{AhoCorasick};


fn main() {

    let input: &str = include_str!("./calibration_values.txt");

    let result: u32 = input
        .lines()
        .map(|line| parse_digit(&line))
        .sum();

    println!("{}", result);
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

    let matches: Vec<u32> = ac
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
