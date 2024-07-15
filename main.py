import os
import platform
import argparse

def print_error(message):
    print(f'\033[91mError:\033[0m {message}')

def print_success(message):
    print(f'\033[92mSuccess:\033[0m {message}')

def print_banner():
    print("""
   _____       ___ __  _______ __         
  / ___/____  / (_) /_/ ____(_) /__  _____
  \__ \/ __ \/ / / __/ /_  / / / _ \/ ___/
 ___/ / /_/ / / / /_/ __/ / / /  __(__  ) 
/____/ .___/_/_/\__/_/   /_/_/\___/____/v1
    /_/        x-projetion.org                          
    """)

def split_file_by_lines(input_file, lines_per_file):
    try:
        with open(input_file, 'r') as f:
            data = f.readlines()
    except FileNotFoundError:
        print_error(f"File '{input_file}' not found.")
        return
    except IOError:
        print_error(f"There was a problem reading the file '{input_file}'.")
        return

    output_folder = 'results'
    if not os.path.exists(output_folder):
        try:
            os.makedirs(output_folder)
            print_success(f"Folder '{output_folder}' created successfully.")
        except OSError:
            print_error(f"Failed to create folder '{output_folder}' to store the result files.")
            return

    file_count = 1
    total_files = len(data) // lines_per_file + 1
    for i in range(0, len(data), lines_per_file):
        output_file = os.path.join(output_folder, f'output_{file_count}.txt')
        try:
            with open(output_file, 'w') as f:
                f.writelines(data[i:i + lines_per_file])
            print_success(f'File {output_file} created successfully.')
        except IOError:
            print_error(f"There was a problem writing to the file '{output_file}'. File splitting aborted.")
            return
        file_count += 1

    print(f'\n\033[92mFile splitting completed.\033[0m Total {file_count - 1} files created from {total_files} parts with {lines_per_file} lines per file.')
    if platform.system() == 'Windows':
        input("\nPress Enter to exit...")
    elif platform.system() == 'Linux':
        input("\nPress Enter to continue...")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_banner()
    parser = argparse.ArgumentParser(description='File Splitter by Lines')
    parser.add_argument('-f', '--files', dest='input_file', required=True, help='Input file name')
    parser.add_argument('-l', '--lines', dest='lines_per_file', type=int, required=True, help='Number of lines per file')
    args = parser.parse_args()

    

    try:
        if args.lines_per_file <= 0:
            print_error("Number of lines per file must be greater than 0.")
        else:
            split_file_by_lines(args.input_file, args.lines_per_file)
    except ValueError:
        print_error("Number of lines per file must be a numeric value.")

if __name__ == "__main__":
    main()
