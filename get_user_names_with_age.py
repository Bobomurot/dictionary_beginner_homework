def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    user_name = []
    for user in data:
        if user['age'] == age:
            user_name.append(user['name'])
    return user_name

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
age = 27

print(get_user_names_with_age(data, age))