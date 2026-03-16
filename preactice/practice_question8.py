def generate_number_triangle(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        row = str(i) * i
        result.append(row)
    return result
