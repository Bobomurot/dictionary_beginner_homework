def get_user_names_with_age_range(data:list, min_age:int, max_age:int) -> list:
    """
    Return a list of users with a given age range

    Args:
        data (dict): A dictionary of values
        min_age (int): The minimum age to search for
        max_age (int): The maximum age to search for
    Returns:
        list: A list of users with the given age range
    """
    user = []
    for person in data:
        if person['age'] >= min_age and person['age'] <= max_age:
            user.append(person['name'])
    return user

data = [
  {
    'name': 'Anny', 
    'age': 20
  }, 
  {
    'name': 'Mary', 
    'age': 30
  }
]
min_age = 20
max_age = 30

print(get_user_names_with_age_range(data, min_age, max_age))