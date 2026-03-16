def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    return ["*" * n for _ in range(n)]
##here underscore _ is used as a throwaway variable in the list comprehension.its a common convention in Python to indicate that the variable is intentionally being ignored.
## Example usage:
# print(generate_square(3)) # Output: ['***', '***', '***'] # print(generate_square(5)) # Output: ['*****', '*****', '*****', '*****', '*****']