import os
import re

def replace_last_n_chars(match):
    """
    This is a hacky script that gets the job done
    However, function must be modified manually
    """
    n = 3  # n=1 for single numbers replace decimals to replace with n=3
    replacement_version = '2'
    return match.group()[:-n] + replacement_version  # Replace 'the string with' with the desired replacement character

def replace_version_number(file_path):
    try:
        # Read the file line by line
        with open(file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        # Define the regex pattern
        pattern = r'[A-Za-z]+\.[A-Za-z]+\.\d+\.\d+v\d+\.*\d*'
        # for line in lines:
        #     print(line)


        # Replace matching text with the specified "v number" line by line
        modified_lines = [re.sub(pattern, replace_last_n_chars, line) for line in lines]

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='UTF-8') as file:
            file.writelines(modified_lines)

        print(f"Updated file: {file_path}")

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

def process_directory(directory_path, extensions=None):
    if extensions is None:
        extensions = ['.md', '.txt']

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                replace_version_number(file_path)

# Specify the directory path and the desired "v number"
directory_path = './baselines'

# Process the directory
process_directory(directory_path)
