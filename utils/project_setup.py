import constants.input_label as input_label
import utils.file_methods as file_methods
import subprocess
import os
import config.setup_routes as setup_routes
import config.setup_redux as setup_redux
import config.setup_tailwind as setup_tailwind

def get_project_name():
    dir_name = input(input_label.project_name)

    if dir_name == "":
        print(input_label.project_name_empty)
        dir_name = get_project_name()
    return dir_name

def set_project(path,dir_name):
    if dir_name == "":
        dir_name = get_project_name()
    
    file_methods.make_dir_if_not_exist(path)

    project_dir = "{}/{}".format(path,dir_name)
    
    is_exist = file_methods.dir_exist_check(path,dir_name)
    if not is_exist or True:
        is_create = input_label.question_yn(input_label.project_exist_false)
        if is_create == "y":
            create_react_project(path,dir_name)
        else:
            file_methods.create_dir(path,dir_name)
    
    is_default_setup = input_label.question_yn(input_label.is_project_setup)
    if is_default_setup == "y":
        file_methods.create_folder_structure("{}/{}".format(project_dir,"src"))
        setup_routes.main(project_dir)
        setup_redux.main(project_dir)
        setup_tailwind.main(project_dir)
    else:
        print("Customization is not implemented yet!")
    
    

def create_react_project(path, dir_name):
    file_methods.make_dir_if_not_exist(path)
    try:
        # Create React App
        command = "npx create-react-app {}".format(dir_name)
        file_methods.run_command(path,command)
    except Exception as e:
        print(f"Error: {e}")
    