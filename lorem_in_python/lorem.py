import random
import os

def generate_lorem_ipsum(num_lines, output_dir="generated_text", filename="lorem.txt", line_length=70):
    """
    Generates a specified number of lines of random characters, mimicking Lorem Ipsum.

    Args:
        num_lines (int): The number of lines to generate in the output file.
        output_dir (str): The directory where the output file will be saved.
                          Defaults to "generated_text".
        filename (str): The name of the output text file. Defaults to "lorem.txt".
        line_length (int): The maximum number of characters per line. Defaults to 70.
    """
    # Using string.ascii_lowercase for a cleaner character set
    # Adding a space at the beginning to ensure spaces appear frequently
    # No need for extra spaces, random.choice will handle distribution
    characters = " " + "abcdefghijklmnopqrstuvwxyz"

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)

    try:
        with open(file_path, "w") as f:
            for _ in range(num_lines): # Use '_' for unused loop variable
                # Use random.choices for a list of characters, then join them
                # This is often more efficient for building strings than repeated concatenation
                line = ''.join(random.choices(characters, k=line_length))
                f.write(line + "\n")
        print(f"Successfully generated {num_lines} lines to '{file_path}'")
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        num_rows = int(input("Enter the number of rows (lines) for your paragraph:\n"))
        if num_rows <= 0:
            print("Please enter a positive number of rows.")
        else:
            # You can customize these arguments if needed
            generate_lorem_ipsum(num_rows)
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of rows.")