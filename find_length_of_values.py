def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    count_values = 0
    for value in data.values():
        if isinstance(value, (str, dict)):
            count_values += len(value)
        
    return count_values

data = {
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }

x = find_length_of_values(data)

print(x)