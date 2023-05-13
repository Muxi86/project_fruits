def get_fruits_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    rows = data.split('\n')[1:]
    ans = []
    for row in rows:
        ans.append(row.split(',')[0])
    return ans

data = open('fruits.csv').read()
print(get_fruits_name(data))
    