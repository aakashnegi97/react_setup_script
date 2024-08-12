from utils.file_methods import dir_exist_check,create_dir
import utils.project_setup as project_setup

def main():

    try:
        path = "/practice/react"
        project_setup.set_project(path,"")


    except Exception as e:
        print(f"An error occurred: {e}")
        return None



if __name__ == "__main__":
    main()