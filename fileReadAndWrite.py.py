# A program that reads a file and writes a modified version of it to another file.
def read_and_write_file(file_name, new_file_name, new_content):
    try:
        # reading the content of the original file
        with open(file_name, 'r') as file:
            content = file.read()
     
     # modifying the content       
        modified_content = content + new_content

    # writing the modified content to a new file
        with open(new_file_name, 'w') as new_file:
            new_file.Write(modified_content)

        print(f"Content from {file_name} has been modified and written to {new_file_name}.")
    except FileNotFoundError:
        print(f"Error: The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        file.close()
        new_file.close()
    
