def generate_hollow_square(n):
    """
    Returns a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    if n == 1:
        return ["*"]
    if n == 2:
        return ["**", "**"]
    
    # First and last row
    top_bottom = "*" * n
    
    # Middle rows
    middle = "*" + " " * (n - 2) + "*"
    
    # Construct full square
    result = [top_bottom] + [middle] * (n - 2) + [top_bottom]
    
    return result
