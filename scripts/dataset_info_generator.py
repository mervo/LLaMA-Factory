import os
import json


def generate_dataset_info_from_jsons(root_dir):
    try:
        # List all files and directories in the given root directory
        items = os.listdir(root_dir)
        # print(items)
    except PermissionError:
        # Skip directories without access permission
        return

    # Iterate over each item in the current directory
    data = {}

    for filename in sorted(items):
        item_path = os.path.join(root_dir, filename)
        # print(filename)

        data[filename] = {
            "file_name": f"{item_path}",
            "formatting": "sharegpt",
            "columns": {
                "messages": "messages",
                "images": "images"
            },
            "tags": {
                "role_tag": "role",
                "content_tag": "content",
                "user_tag": "user",
                "assistant_tag": "assistant"
            }
        }

    print(json.dumps(data, indent=4))

    with open('dataset_info.json', 'w') as file:
        json.dump(data, file, indent=4)

# Specify the directory path to start from (e.g., '.')
root_directory = '/mnt/c/Users/user/Documents/datasets/dataset_20200803/json'
generate_dataset_info_from_jsons(root_directory)
