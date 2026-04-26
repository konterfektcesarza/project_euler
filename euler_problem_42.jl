alphabet = Dict{Char,UInt16}()

for (n, l) in enumerate(collect('a':'z'))
    alphabet[l] = n
end

source = split(read(raw"C:\Users\hajdu\Downloads\words.txt", String), ",")
source = lowercase.(source)

counter = 0

for word in source
    global counter
    letters = collect(word)
    total = sum([alphabet[l] for l in letters if l != '"'])
    to_check = (sqrt(1 + 8 * total) - 1) / 2
    if isinteger(to_check)
        counter += 1
    end
end

println(counter)
