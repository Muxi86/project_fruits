import csv
def get_cheapest_fruit(data: str) -> str:
    """
    This function returns the name of the cheapest fruit

    args:
        data: CSV file with the fruits data
    returns:
        str: name of the cheapest fruit
    """
    # your code here
    reader = csv.reader(open(data))
    next(reader)

    ans = []
    for row in reader:
        ans.append(float(row[1]))

    return min(ans)

print(get_cheapest_fruit('fruits.csv'))