def generate_rectangle(n, m):
    """
    Returns a rectangle pattern of '*' of size n x m as a list of strings.
    
    Parameters:
    n (int): Number of rows (length).
    m (int): Number of columns (breadth).
    
    Returns:
    list: A list of strings where each string represents a row of the rectangle.
    """
    row = "*" * m         # Create a single row of m stars
    rectangle = [row] * n # Repeat it n times to form n rows
    return rectangle
##very similar to generate_square function in practice_question1.py
##[] represents a list in Python