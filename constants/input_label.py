project_dir = "Enter project directory of your react app: "
project_name = "Enter project name of your react app: "
project_name_empty = "Project name can't be empty!"
project_exist_false = "Project doesn't exist, want to create it from scratch? (y/n) "
is_project_setup = "Setup project default? (y/n)"
expected_yn = "Expected y/n."

def question_yn(label):
    response = input(label)
    if response not in ["y","n"]:
        print(input_label.expected_yn)
        return question_yn(label)
    return response

def package_already_setup_message(package_name = ""):
    return "Package already installed {}.".format(package_name)