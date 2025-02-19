def sum_dict_values(data: dict) -> int:
    '''
    Return the sum of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of all values in the dictionary
    '''
    
    return sum(data.values())

data = {
    'a': 1, 
    'b': 2, 
    'c': 3
  }

print(sum_dict_values(data))