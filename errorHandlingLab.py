# Ask user for file name and handle errors if file does not exist or cannot be read.
def user_input_file():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        file.close()