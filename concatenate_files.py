import os

def concatenate_files(output_file, specific_files):
    files_found = 0
    with open(output_file, 'w') as outfile:
        for specific_file in specific_files:
            if os.path.isfile(specific_file):
                files_found += 1
                print(f'Reading file: {specific_file}')
                with open(specific_file, 'r') as infile:
                    outfile.write(f'\n\n# Begin {specific_file}\n')
                    outfile.write(infile.read())
                    outfile.write(f'\n# End {specific_file}\n')
            else:
                print(f'File not found: {specific_file}')
    if files_found == 0:
        print(f'No specified files found in the given list.')
    else:
        print(f'All code files have been concatenated into {output_file}')

specific_files = [
    'app/templates/component.jsx',
    'app/templates/index.html',
    'app/__init__.py',
    'app/model.py',
    'app/views.py',
    'app/webscrape.py',
    'main.py'
]

output_filename = 'combined_code.txt'

# Call the function to concatenate files
concatenate_files(output_filename, specific_files)
