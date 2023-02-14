def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    x = 0
    for i in data:
        for k in i:
            if i[k] == age:
                x += 1
    return x
data = [
  {
    'name': 'John', 
    'age': 35
  },
  {
    'name':'Mary', 
    'age': 20
  }
  ]
print(count_users_with_age(data, 38))