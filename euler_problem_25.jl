n₁ = BigInt(1)
n₂ = BigInt(1)
lₙ = 0
term = 2

while lₙ < 1000
    global n₁, n₂, lₙ, term
    n₁, n₂ = n₂, n₁ + n₂
    term += 1
    lₙ = length(string(n₂))
end

print(term)
