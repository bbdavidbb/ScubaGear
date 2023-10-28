import os
import re

CHARS_TO_REPLACE = 1 # n=1 for single numbers; replace with n=3 for decimals
REPLACEMENT_VERSION ='1'

def replace_last_n_chars(match):
    """
    This is a hacky script that gets the job done
    However, function must be modified manually
    """
    return match.group()[:-CHARS_TO_REPLACE] + REPLACEMENT_VERSION  # Replace 'the string with' with the desired replacement character

def replace_version_number(file_path):
    try:
        # Read the file line by line
        with open(file_path, 'r', encoding='UTF-8') as file:
            lines = file.readlines()

        # Define the regex pattern
        pattern = r'[A-Za-z]+\.[A-Za-z]+\.\d+\.\d+v\d+\.*\d*'

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
        extensions = ['.md', '.rego', '.ps1']

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                replace_version_number(file_path)

# Specify the directory path and the desired "v number"
baseline_path = './baselines'
rego_path ='./Rego'
testing_path ='./Testing'

# Process the directory
process_directory(baseline_path)
# process_directory(rego_path)
# process_directory(testing_path)
