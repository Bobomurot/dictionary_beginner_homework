import json

def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    count_jobs = 0
    for user_data in data:
        if "job" in user_data:
            if user_data["job"] == job:
                count_jobs += 1
    return count_jobs

data=[
  {
    'name': 'John', 
    'job': 'Developer'
  }, 
  {
    'name': 'Mary', 
    'job': 'Developer'
  }
  ]

job = 'Developer'

print(count_jobs(data, job))