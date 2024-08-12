import constants.input_label as input_label
import utils.file_methods as file_methods
import subprocess
import os

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
    
    is_exist = file_methods.dir_exist_check(path,dir_name)
    if not is_exist:
        is_create = input(input_label.project_exist_false)
        if is_create not in ["y","n"]:
            print(input_label.expected_yn)
            set_project(path,dir_name)
            return
        elif is_create == "y":
            create_react_project(path,dir_name)
        else:
            file_methods.create_dir(path,dir_name)
    

def create_react_project(path, dir_name):
    file_methods.make_dir_if_not_exist(path)
    try:
        command = "npx create-react-app {}".format(dir_name)
        file_methods.run_command(path,command)
    except Exception as e:
        print(f"Error: {e}")


    