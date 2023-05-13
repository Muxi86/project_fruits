import csv
def get_fruits_name(data:str)->list:
    """
    This function returns the names of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        list: list of fruits names
    """
    reader = csv.reader(open(data))
    next(reader)
    ans = []
    for row in reader:
        ans.append(row[0])
    return ans

print(get_fruits_name('fruits.csv'))
    