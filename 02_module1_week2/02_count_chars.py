# Write a function to output a dictionary
# in which key is a char and value is a counting number of char
def count_chars(string: str) -> dict:
    """Count number of chars."""
    if not isinstance(string, str):
        raise TypeError("string must be a string type.")

    m = {}
    for char in string:
        if char not in m.keys():
            m[char] = 1
        else:
            m[char] += 1

    return m


if __name__ == "__main__":
    string = "similes"
    res = count_chars(string)
    print(res)
