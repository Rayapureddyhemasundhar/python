def generate_triangle(n):
    """
    Returns a right-angled triangle pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    triangle = []               # Create an empty list to store rows
    for i in range(1, n + 1):   # Loop from 1 to n
        row = "*" * i           # Create a string with i stars
        triangle.append(row)    # Add it to the list
    return triangle
