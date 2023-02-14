def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    x = 0
    for i in data:
        for k in i:
            if i[k] == job:
                x += 1
    return x
    
data = [
  {
    'name': 'John',
    'job': 'Barber'
  }, 
  {
    'name': 'Mary',
    'job': 'Developer'
  },
  {
    'name': 'Ann', 
    'job': 'Teacher'
  }
  ]
print(count_jobs(data, 'Student'))