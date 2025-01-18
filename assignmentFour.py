def modify_content(content):
    # code to turn the content to uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the filename
        input_file = input("Enter the filename to read: ").strip()
        
        # Attempt to open and read the file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_content(content)
        
        # Define the output filename
        output_file = input("Enter the filename to save the modified content: ").strip()
        
        # Write the modified content to the new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{input_file}' or write to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
