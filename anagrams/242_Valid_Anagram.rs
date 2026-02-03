use std::collections::HashMap;
// https://doc.rust-lang.org/rust-by-example/std/hash.html

// 1. You must define the struct 'Solution' before you can 'impl' it.
struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        // Optimization for LeetCode: if lengths differ, they can't be anagrams
        if s.len() != t.len() { return false; }

        let mut counter: HashMap<char, usize> = HashMap::new();
        for c in s.chars() {
            let count = counter.entry(c).or_insert(0);
            *count += 1;
        }

        for c in t.chars() {
            let count = counter.entry(c).or_insert(0);
            *count -= 1;
            // 2. We must dereference 'count' to compare it to 0
            if *count == 0 {
                // 3. .remove() takes a reference (&c)
                counter.remove(&c);
            }
        }

        // 4. Return whether the map is empty (Implicit return - no semicolon)
        counter.is_empty()
    }
}

fn main() {
    // 5. String literals are &str, but function expects String. Use .to_string()
    assert!(Solution::is_anagram("123abc".to_string(), "abc123".to_string()));
}