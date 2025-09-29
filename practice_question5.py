def generate_inverted_triangle(n):
    """
    Returns an inverted right-angled triangle pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    triangle = []               # Empty list to store rows
    for i in range(n):
        row = "*" * (n - i)     # Each row has n-i stars
        triangle.append(row)    # Add the row to the list
    return triangle
