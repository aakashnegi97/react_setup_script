from utils.file_methods import dir_exist_check,create_dir
import utils.project_setup as project_setup
import constants.input_label as input_label

def main():

    try:
        dir_path = input(input_label.project_dir)
        if dir_path == "":
            main()
            return
        project_setup.set_project(dir_path,"")


    except Exception as e:
        print(f"An error occurred: {e}")
        return None



if __name__ == "__main__":
    main()