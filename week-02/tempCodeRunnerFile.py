def solve(a, b, c, d):
    if (
        a + b * c == d or
        a + b - c == d or
        a - b + c == d or
        a - b * c == d or
        a * b + c == d or
            a * b - c == d):
        return "YES"

    return "NO"


# Input and Output
a, b, c, d = map(int, input().split())
print(solve(a, b, c, d))
