import os
import json
import shutil

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

def check_dependency(project_dir, dependency_name):
    # Open and read the package.json file
    package_json_path = "{}/{}".format(project_dir,"package.json")
    try:
        with open(package_json_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("The file package.json does not exist.")
        return False
    except json.JSONDecodeError:
        print("Error decoding JSON from the package.json file.")
        return False

    # Check if the dependency is in either 'dependencies' or 'devDependencies'
    dependencies = data.get('dependencies', {})
    dev_dependencies = data.get('devDependencies', {})
    
    return (dependency_name in dependencies) or (dependency_name in dev_dependencies)


def create_folder_structure(project_dir):

    # Create component
    make_dir_if_not_exist("{}/{}".format(project_dir,"components"))

    # Create routes
    make_dir_if_not_exist("{}/{}".format(project_dir,"routes"))

    # Create pages
    make_dir_if_not_exist("{}/{}".format(project_dir,"pages"))

    # Create redux
    make_dir_if_not_exist("{}/{}".format(project_dir,"redux"))

    # Create assets
    make_dir_if_not_exist("{}/{}".format(project_dir,"assets"))

    # Create utils
    make_dir_if_not_exist("{}/{}".format(project_dir,"utils"))

def copy_paste_file(source_path,destination_path):
    # Copy the file
    shutil.copy(source_path, destination_path)
    print(f"File copied from {source_path} to {destination_path}")