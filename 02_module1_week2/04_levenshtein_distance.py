# Find the minumun distance to transform S string to T string
# This is known as Levenshtein distance
def calc_levenshtein_distance(s: str, t: str) -> int:
    m, n = len(s), len(t)

    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                D[i][j] = min(D[i - 1][j - 1], D[i][j - 1], D[i - 1][j])
            else:
                D[i][j] = min(D[i - 1][j - 1], D[i][j - 1], D[i - 1][j]) + 1

    # print(D)
    return D[m][n]


if __name__ == "__main__":
    s = "kitten"
    t = "sitting"
    res = calc_levenshtein_distance(s, t)
    print(res)
