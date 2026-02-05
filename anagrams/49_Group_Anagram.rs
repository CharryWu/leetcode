use std::collections::HashMap;
// https://doc.rust-lang.org/rust-by-example/std/hash.html

// 1. You must define the struct 'Solution' before you can 'impl' it.
struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hashmap: HashMap<String, Vec<String>> = HashMap::new();
        let mut grouped: Vec<Vec<String>> = Vec::new();

        for s in strs {
            let mut sorted: Vec<char> = s.chars().collect();
            sorted.sort();
            let sorted = sorted.into_iter().collect::<String>();
            hashmap.entry(sorted).or_insert(vec![]).push(s);
        }

        for (_key, value) in hashmap {
            grouped.push(value);
        }

        grouped
    }
}

fn main() {
    // 5. String literals are &str, but function expects String. Use .to_string()
    println!("{:?}",
        Solution::group_anagrams(
            vec![
                "eat".to_string(),
                "tea".to_string(),
                "tan".to_string(),
                "ate".to_string(),
                "nat".to_string(),
                "bat".to_string(),
            ]));
}