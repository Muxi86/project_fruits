import csv
def get_total_price(fname:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """

    data = open(fname)
    reader = list(csv.reader(data))
    ans = 0
    for row in reader[1:]:
        ans += float(row[1])
    return ans

print(get_total_price('fruits.csv'))