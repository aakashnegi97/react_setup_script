import os

def dir_exist_check(path, dir_name):
    dir_path = os.path.join(path, dir_name)
    return os.path.isdir(dir_path)

def create_dir(path,dir_name):
    dir_path = os.path.join(path, dir_name)
    os.makedirs(dir_path, exist_ok=True)

def make_dir_if_not_exist(path):
    if not dir_exist_check(path,""):
        create_dir(path,"")

def run_command(path, command):
    # Ensure the outer directory exists
    make_dir_if_not_exist(path)
    # Run the command in the outer directory
    try:
        os.chdir(path)
        # Run the command
        os.system(command)
        print(f"Command ran successfully in '{path}'")
    except Exception as e:
        print(f"Error : {e}")