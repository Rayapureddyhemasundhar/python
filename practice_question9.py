def generate_floyds_triangle(n: int) -> list[str]:
    """
    Generates the first n rows of Floyd's Triangle.

    Args:
        n: The number of rows to generate.

    Returns:
        A list of strings, where each string represents a row of the triangle.
    """
    # This list will store the final list of row strings
    triangle_rows = []
    # This variable keeps track of the next number to be placed in the triangle
    current_number = 1

    # The outer loop iterates for each row we need to create (from row 1 to row n)
    for i in range(1, n + 1):
        # This temporary list will hold the numbers for the current row
        row_numbers = []
        
        # The inner loop runs 'i' times, because row 'i' has 'i' numbers
        # For example, row 3 has 3 numbers, row 4 has 4 numbers, etc.
        for _ in range(i):
            # Add the current number (as a string) to our temporary list
            row_numbers.append(str(current_number))
            # Increment the number for the next position
            current_number += 1
            
        # Join the numbers in the list with a space to form a single string
        row_string = " ".join(row_numbers)
        # Add the completed row string to our final list
        triangle_rows.append(row_string)
        
    return triangle_rows