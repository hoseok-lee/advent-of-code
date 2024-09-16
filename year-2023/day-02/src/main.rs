extern crate regex;

use regex::Regex;
use std::collections::HashMap;
use std::cmp;


fn main() {
    let input: &str = include_str!("./game_records.txt");

    let part_one: usize = input
        .lines()
        .enumerate()
        .map(
            |(i, line)| match check_games(&line) {
                true => i + 1,
                false => 0
            }
        )
        .sum();

    let part_two: u32 = input
        .lines()
        .map(|line| compute_power(&line))
        .sum();

    println!("{}, {}", part_one, part_two);
}

fn check_games(haystack: &str) -> bool {

    let bag_limit: HashMap<&str, u32> = HashMap::from([
        ("red", 12),
        ("green", 13),
        ("blue", 14)
    ]);

    let re = Regex::new(
        r"([0-9]+) (red|green|blue)"
    ).unwrap();

    let result = re
        .captures_iter(haystack)
        .all(
            |caps| {
                let bag_color: &str = caps
                    .get(2)
                    .unwrap()
                    .as_str();

                let number_of_cubes: u32 = caps
                    .get(1)
                    .unwrap()
                    .as_str()
                    .parse()
                    .unwrap();

                // Ensure that all pulls meet requirements
                bag_limit.get(bag_color).unwrap() >= &number_of_cubes
            }
        ); result

}

fn compute_power(haystack: &str) -> u32 {

    let mut amount_per_color: HashMap<&str, u32> = HashMap::new();

    let re = Regex::new(
        r"([0-9]+) (red|green|blue)"
    ).unwrap();

    for caps in re.captures_iter(haystack) {

        let bag_color: &str = caps
            .get(2)
            .unwrap()
            .as_str();

        let number_of_cubes: u32 = caps
            .get(1)
            .unwrap()
            .as_str()
            .parse()
            .unwrap();

        // Store total number of cubes per color
        let accumulated_cubes = amount_per_color
            .entry(bag_color)
            .or_insert(0);

        *accumulated_cubes = cmp::max(*accumulated_cubes, number_of_cubes)
    }

    amount_per_color.values().product()

}