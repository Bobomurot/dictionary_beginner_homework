def sum_float_values(data: dict) -> float:
    '''
    Return the sum of all float values in dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        float: The sum of all float values in the dictionary.
    '''
    float_sum = 0
    for value in data.values():
        if isinstance(value, float):
            float_sum += value
    return float_sum

data = {
    'a': 1, 
    'b' : 2.5, 
    'c': 3.0
  }

print(sum_float_values(data))