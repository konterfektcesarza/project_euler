// Euler problem 34
// https://projecteuler.net/problem=34
// Find the sum of all numbers which are equal to the sum of the factorial of their digits.

// First - what is the upper bound needed for the programme to be complete?
// It is clear that (9! * n) increases slower than 10^^(n-1) with lim n -> infinity
// Thus we may notice that at some n it is no longer possible for (9! * n) [maximum variant for factorials sum] to equal 10^^(n-1)
// We run a simple python script to determine what the upper n is:

/*
import math

n = 1
while math.factorial(9)*n > 10**(n-1):
    n += 1

print(n)
 */

// Out = 8
// Thus we conlcude that we do not have to search through numbers higher than max variant = 9_999_999

fn main() {
    let mut found = Vec::new();
    for i in 10..=9_999_999 {
        if factor_sum(i) == i {
            found.push(i);
        }
    }
    let ret = found.iter().sum::<usize>();
    println!("{:?}", ret);
}

fn factor_sum(n: usize) -> usize {
    n
    .to_string()
    .chars()
    .map(|d| factorial(d.to_digit(10).unwrap() as usize))
    .sum::<usize>()
}


fn factorial(a: usize) -> usize {
    let mut ret = 1;
    for i in 2..=a {
        ret *= i;
    }
    ret
}
