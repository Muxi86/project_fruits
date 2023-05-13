import csv
def get_fruits(file_path: str):
    """
    Reads the file file_path and returns a list of fruits
    
    Args:
        file_path (str): absolute file path
    Returns:
        list: list of fruits
    """
    reader = csv.reader(open(file_path))
    next(reader)

    ans = []
    for row in reader:
        ans.append(row)
    return ans

print(get_fruits('fruits.csv'))