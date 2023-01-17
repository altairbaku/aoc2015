with open('input.txt') as f:
    lines = f.readlines()

def p1(string_literals):
    p1 = 0
    for line in string_literals:
        string_literal = line.strip()
        strip_quotes = string_literal[1:-1]
        n = 0
        mem_len = 0
        while n < len(strip_quotes):
            if strip_quotes[n:n+2] == "\\x":
                n += 4
            elif strip_quotes[n:n+2] == "\\\"" or strip_quotes[n:n+2] == "\\\\":
                n += 2
            else:
                n += 1
            mem_len += 1
        p1 += (len(string_literal) - mem_len)
    return p1

def p2(string_literals):
    p2 = 0
    for line in string_literals:
        string_literal = line.strip()
        p2 += (4 + (string_literal.count("\"")- 2) + string_literal.count("\\"))
    return p2



print(p1(lines))
print(p2(lines))
