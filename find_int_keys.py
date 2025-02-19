import json

def find_int_keys(data: dict) -> list:
    """
    Return a list of all keys in a dictionary that are integers.
    Args:
        data (dict): A dictionary of values
    Returns:
        list: A list of all keys in the dictionary that are integers.
    """
    count = []
    for key in data:
        if isinstance(key, int):
            count.append(key)
    return count

data = {
    "x": "23",
    "3": "y", 
    "z": "5", 
    7:'a'
  }
x = find_int_keys(data)
print(x)