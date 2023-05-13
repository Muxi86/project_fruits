import csv
def get_expensive_fruit(data: str) -> str:
    """
    This function returns the name of the most expensive fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the most expensive fruit
    """
    # your code here
    reader = csv.reader(open(data))
    next(reader)
    
    ans = []
    for row in reader:
        ans.append(float(row[1]))
    return max(ans)

print(get_expensive_fruit('fruits.csv'))


