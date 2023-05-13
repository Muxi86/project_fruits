def get_fruits(file_path: str):
    """
    Reads the file file_path and returns a list of fruits
    
    Args:
        file_path (str): absolute file path
    Returns:
        list: list of fruits
    """
    rows = file_path.split('\n')[1:]
    
    ans = []
    for row in rows:
        ans.append(row)
    return ans

file_path = open('fruits.csv').read()
print(get_fruits(file_path))