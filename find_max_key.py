def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    a = []
    for i in data:
        if type(i)==int or type(i)==float:
            a.append(i)
    mx = a[0]
    for i in a[1:]:
        if i>mx:
            mx = i
    return mx
data = {
    1.4 :'a', 
    7.8 :'b', 
    4 : 'c'
  }
print(find_max_key(data))