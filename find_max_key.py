def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    max_key = max(data.keys())
    return max_key

data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }

x = find_max_key(data)
print(x)