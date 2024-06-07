

def get_max_profit(values: list[int], boxes: list[int], t_size: int):
    max_profit = 0
    d = {v: boxes[i] for i, v in enumerate(values)}
    values.sort(reverse=True)

    for v in values:
        if t_size == 0:
            break
        b_size = min(d[v], t_size)
        max_profit += b_size * v
        t_size -= b_size

    return max_profit


if __name__ == "__main__":
    print(get_max_profit([2, 7, 4], [3, 1, 6], 5))
