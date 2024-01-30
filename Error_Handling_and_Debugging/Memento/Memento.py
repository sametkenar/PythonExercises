def memento(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            try:
                number = int(content)
                return f"Finally you found the correct one! The password is: {number}"
            except ValueError:
                return "Wrong file, try again!"
    except FileNotFoundError:
        return "File not found, try again!"

# Example usage
file_path = "test1.txt"
file_path1 = "test2.txt"
result = memento(file_path)
result1 = memento(file_path1)
print(result)
print(result1)
