/*

# Problem:  https://projecteuler.net/problem=23 

function for proper divisors 

function for perfect/deficient/abudnat number

function problem
*/

// 

fn proper_divisors(dzielona:u32) -> Vec<u32> {
    let bound: u32 = (dzielona as f64).sqrt() as u32;
    let mut dzielniki: Vec<u32> = vec![1];

    for i in 2..=bound {
        let potencjal: u32 = dzielona / i;
        if dzielona % i == 0 {
            dzielniki.push(i);
            if potencjal != i {
                dzielniki.push(dzielona/i);
            }
        }
    }
    return dzielniki
}

fn suma(obiekt:Vec<u32>) -> u32 {
    let mut sumka: u32 = 0;
    for i in obiekt {
        sumka += i;
    }
    return sumka
}

fn is_abundant(numba:u32) -> bool {
    
    let divs: Vec<u32> = proper_divisors(numba);
    let sprawdz: u32 = suma(divs);
    
    if sprawdz > numba {
        return true
    }
    else {
        return false
    }
}

fn main() {
    let mut abundants: Vec<u32> = Vec::new();
    let mut sum_2_abundants = vec![false; 28124];

    for i in 1..=28123 {
        if is_abundant(i) {
            abundants.push(i);
        }
    }

    for a in 0..abundants.len() {
        for b in a..abundants.len() {
            let pot: u32 = abundants[a] + abundants[b];
            if pot <= 28123 {
                sum_2_abundants[pot as usize] = true;
            }
            else {
                break
            }
        }
    }

    let result: u32 = (1..=28123)
    .filter(|&i| !sum_2_abundants[i as usize])
    .sum();
    
    println!("The answer is: {}", result)
}