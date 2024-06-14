# Simple sliding window inside a list
def sliding_window(num_list: list, k: int) -> int:
    """Finding the maximum of sliding window with size k in a list."""

    res = []
    for i in range(len(num_list)-k+1):
        res.append(max(num_list[i:i + k]))

    return max(res)


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    res = sliding_window(num_list, k)
    print(res)
