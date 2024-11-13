import os
import json

definitions = {
    "ccd": "CHARGE-COUPLED DEVICE (CCD)",
    'swir': "SHORT-WAVE INFRARED (SWIR)",
    'mwir': "MEDIUM-WAVE INFRARED (MWIR)",
}


def display_tree_structure(root_dir):
    try:
        # List all files and directories in the given root directory
        items = os.listdir(root_dir)
        # print(items)
    except PermissionError:
        # Skip directories without access permission
        return

    # Iterate over each item in the current directory
    for spectrum in sorted(items):
        # classes, 1 json per class
        sensor = ' '.join(definitions.get(word, word)
                          for word in spectrum.split())
        item_path = os.path.join(root_dir, spectrum)
        if os.path.isdir(item_path):
            classes = os.listdir(item_path)
            for cur_class in classes:
                item_path_path = os.path.join(item_path, cur_class)
                filenames = os.listdir(item_path_path)  # filenames
                user = {
                    "content": "<image> describe this image",
                    "role": "user"
                }
                assistant = {
                    "content": f"This is a {cur_class} from the {sensor} sensor.",
                    "role": "assistant"
                }

                messages = []
                images = []
                for cur_filename in filenames:
                    messages.append(user)
                    messages.append(assistant)
                    images.append(os.path.join(item_path_path.replace(
                        '/mnt/c/Users/user/Documents/datasets', '/app/data'), cur_filename))
                data = [
                    {
                        "messages": messages,
                        "images": images
                    }
                ]

                with open(f'{spectrum}_{cur_class}.json', 'w') as file:
                    json.dump(data, file, indent=4)


# Specify the directory path to start from (e.g., '.')
# Replace with the directory you want to inspect
root_directory = '/mnt/c/Users/user/Documents/datasets/dataset_20200803'
display_tree_structure(root_directory)
