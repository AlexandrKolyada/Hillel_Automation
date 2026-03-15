import os
import json
import  logging

logging.basicConfig(filename='json__kolyada.log', level=logging.ERROR, format='%(levelname)s - %(message)s')

folder_path = 'ideas_for_test/work_with_json'

files = os.listdir(folder_path)

for filename in files:
    print(f"Find file: {filename}")

for filename in  files:
    file_path = os.path.join(folder_path, filename)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
            print(f"File {filename} is valid")

    except json.JSONDecodeError:
        error_message = f"File {filename} do not is valid JSON"
        logging.error(error_message)
        print(f"File {filename} broken. Error write in log")