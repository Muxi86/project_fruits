import csv
def get_cheapest_fruit_id(data: str) -> int:
    """
    This function returns the index of the cheapest fruit

    args:
        data (str): CSV file with the fruits data
    returns:
        int: id of the cheapest fruit
    """
    # your code here
    data = open('fruits.csv')
    reader = list(csv.reader(data))
    
    
    return reader
    
print(get_cheapest_fruit_id('fruits.csv'))