def generate_pyramid(n):
    """
    Returns a centered pyramid pattern of '*' of height n as a list of strings.
    
    Parameters:
    n (int): Number of rows in the pyramid.
    
    Returns:
    list: A list of strings representing the pyramid.
    """
    pyramid = []
    max_width = 2 * n - 1        # width of the base row

    for i in range(1, n + 1):
        stars = "*" * (2 * i - 1)                 # number of stars in row i
        spaces = " " * ((max_width - len(stars)) // 2)  # spaces to center
        row = spaces + stars + spaces             # construct row
        pyramid.append(row)
    
    return pyramid
