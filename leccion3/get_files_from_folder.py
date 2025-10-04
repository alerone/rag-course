import os 

def get_files_from_folder(folder_path):
    files = []
    for name in os.listdir(folder_path):
        route = os.path.join(folder_path, name)
        if os.path.isfile(route):
            files.append(route)
    return files
