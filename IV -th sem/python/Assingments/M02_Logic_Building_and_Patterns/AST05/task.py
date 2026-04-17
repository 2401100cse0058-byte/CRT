def number_triangle(n: int) -> str:
    lines = []

    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line += str(j)
        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))