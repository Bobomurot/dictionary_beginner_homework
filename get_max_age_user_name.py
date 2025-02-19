def get_max_age_user_name(data:list) -> str:
    """
    Return the name of the user with the maximum age in a dictionary.

    Args:
        data (dict): A dictionary of values
    Returns:
        str: The name of the user with the maximum age in the dictionary
    """
    if not data:
        return None
    
    max_age_user = data[0]
    
    for user in data:
        if user['age'] > max_age_user['age']:
            max_age_user = user

    return max_age_user['name']

data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]

print(get_max_age_user_name(data))