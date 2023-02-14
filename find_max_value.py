def find_max_value(data: dict):
    """
    Return the maximum int or float value in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum value in the dictionary.
    """
    a = []
    for i in data:
        if type(data[i])==int or type(data[i])==float:
            a.append(data[i])
    mx = a[0]
    for i in a[1:]:
        if i>mx:
            mx = i
    return mx
data  = {
    'a' : -4, 
    'b' : -10, 
    'c' : 0
  }
print(find_max_value(data))