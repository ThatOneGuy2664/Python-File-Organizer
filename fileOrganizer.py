import os
import shutil
from collections import defaultdict

file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.txt', '.pdf', '.docx', '.xlsx', '.pptx', '.md', '.doc'],
    'Audio': ['.mp3', '.wav', '.flac', '.ogg', '.aac', '.aif', '.aiff'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Archives': ['.zip', '.tar', '.rar', '.7z'],
    'Java': ['.java', '.jar', '.class'],
    'Python': ['.py', '.whl', '.egg', '.pyc', '.pyd'],
    'Lua': ['.lua'],
    'CSS': ['.css'],
    'TypeScript': ['.ts'],
    'Rust': ['.rs'],
    'C': ['.c', '.h'],
    'C++': ['.cpp', '.hpp', '.C', '.cc',  '.cxx'],
    'Cython': ['.pyx'],
    'HTML': ['.html'],
    'JavaScript': ['.js'],
    'Executables': ['.exe', '.bat', '.bin', '.sh'],
    'Installers': ['.msi', '.apk'],
    'Other': []
}

def organize_files(directory):
    files_by_type = defaultdict(list)
    script_filename = os.path.basename(__file__)
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        if os.path.isfile(filepath) and filename != script_filename:  # Ignore directories and the script itself
            file_ext = os.path.splitext(filename)[1].lower()
            categorized = False
            for category, extensions in file_types.items():
                if file_ext in extensions:
                    files_by_type[category].append(filename)
                    categorized = True
                    break
            if not categorized:
                files_by_type['Other'].append(filename)

    for category, files in files_by_type.items():
        category_folder = os.path.join(directory, category)
        os.makedirs(category_folder, exist_ok=True)  # Create category folder if it doesn't exist
        
        for file in files:
            src = os.path.join(directory, file)
            dst = os.path.join(category_folder, file)
            print(f"Moving {file} to {category_folder}")
            shutil.move(src, dst)

def main():
    while True:
        directory = input("Enter the directory to organize (leave blank to use the current script's directory, type 'exit' to quit):\n")
        
        if directory.lower() == "exit":
            print("Exiting the program.")
            break
        
        if directory == "":
            directory = os.path.dirname(os.path.abspath(__file__))  # Use the script's directory if no input is given
        
        if os.path.isdir(directory):
            print(f"Organizing files in: {directory}")
            organize_files(directory)
            print("Files have been organized.")
        else:
            print("Invalid directory. Please try again.")
        
        print("") # Newline

if __name__ == "__main__":
    main()
