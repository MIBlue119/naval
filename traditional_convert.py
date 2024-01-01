import os
from opencc import OpenCC

def convert_to_traditional_chinese(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        simplified_text = file.read()
    
    # Convert from Simplified to Traditional
    cc = OpenCC('s2twp')
    traditional_text = cc.convert(simplified_text)

    # Write the converted text back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(traditional_text)

def main():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(f"Converting {file_path}...")
                convert_to_traditional_chinese(file_path)
    print("Conversion complete.")

if __name__ == "__main__":
    main()
