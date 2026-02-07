struct Solution;

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let mut temp: i32 = x;
        let mut reversed = 0;

        while temp > 0 {
            let rightmost_digit = temp % 10;
            temp = temp / 10;
            reversed = reversed * 10 + rightmost_digit;
        }

        x == reversed
    }
}

fn main() {
    assert!(Solution::is_palindrome(123) == false);
    assert!(Solution::is_palindrome(121) == true);
    assert!(Solution::is_palindrome(-11) == false);
}