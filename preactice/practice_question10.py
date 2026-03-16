def generate_floyds_triangle(n: int) -> list[str]:
    triangle_rows = []
    current_number = 1
    for i in range(1, n + 1): 
        row_numbers = []
        for _ in range(i):   
            row_numbers.append(str(current_number)) 
            current_number += 1
        row_string = " ".join(row_numbers) 
        x=[]
        x.append(row_string)
        print(x)
    return triangle_rows
print(generate_floyds_triangle(5))