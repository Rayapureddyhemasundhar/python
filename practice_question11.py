def generate_diamond(n):
    """
    Generates a diamond pattern of '*' characters.

    Args:
        n: The number of rows for the upper half of the diamond.

    Returns:
        A list of strings representing the diamond pattern.
    """
    # This list will store all rows of the final pattern
    diamond = []
    # The total width of the diamond is determined by its widest row
    total_width = 2 * n - 1

    # --- Build the upper half and the middle row ---
    # We loop from 1 to n to build each row
    for i in range(1, n + 1):
        # The number of stars in each row follows the pattern 1, 3, 5, ...
        num_stars = 2 * i - 1
        # Create the string of stars
        star_part = '*' * num_stars
        # Use the .center() method to add the correct padding of spaces
        row = star_part.center(total_width)
        diamond.append(row)

    # --- Build the lower half ---
    # The lower half is a mirror of the upper half (excluding the middle row).
    # We can get this by slicing the 'diamond' list to get all rows except the last one,
    # and then reversing that slice.
    lower_half = diamond[:-1][::-1]
    
    # Add the lower half rows to the main diamond list
    diamond.extend(lower_half)
    
    return diamond