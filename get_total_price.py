def get_total_price(data:str)->float:
    """
    This function returns the total price of the fruits

    args:
        data: CSV file with the fruits data
    returns:
        float: fruits total price
    """ 
    rows = data.split('\n')[1:]
    ans = 0
    for row in rows:

        ans += float(row.split(',')[1])
    
    return ans
data = open('fruits.csv').read()
print(get_total_price(data))