import utils.file_methods as file_methods
import constants.input_label as input_label

package1 = "redux"
package2 = "react-redux"
package3 = "@reduxjs/toolkit"
package4 = "redux-thunk"
package5 = "axios"

def main(path):

    try:
        # is_created = file_methods.check_dependency(path,package1)
        if True:

            src_path = "{}/{}".format(path,"src")
            src_redux_path = "{}/{}".format(src_path,"redux")

            # Install Redux
            install_redux(path)

            # Setup Redux
            from_source = "components/redux"
            file = "store.js"
            file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(src_redux_path,file))

            # Actions
            from_action_source = "{}/actions".format(from_source)
            src_redux_path_action = "{}/actions".format(src_redux_path)
        
            file = "index.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}".format(src_redux_path_action,file))
            file = "userAction.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}".format(src_redux_path_action,file))


            # Reducer
            from_action_source = "{}/reducer/user".format(from_source)
            src_redux_path_action = "{}/reducer/user".format(src_redux_path)
        
            file = "actions.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}".format(src_redux_path_action,file))
            file = "userSlice.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}".format(src_redux_path_action,file))

            # Page
            from_action_source = "components/pages"
            src_pages_action = "{}/pages".format(src_path)
        
            file = "Dashboard.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}/{}".format(src_pages_action,"dashboard","index.js"))
            file = "Login.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}/{}".format(src_pages_action,"login","index.js"))
            

            # index.js
            from_action_source = "components"
            src_redux_path_action = "{}".format(src_path)
        
            file = "index.js"
            file_methods.copy_paste_file("{}/{}".format(from_action_source,file),"{}/{}".format(src_redux_path_action,file))


        else:
            print(input_label.package_already_setup_message(package1))


    except Exception as e:
        print(f"Error: {e}")
    
def install_redux(path):
    try:
        command = "npm install {}".format(package1)
        file_methods.run_command(path,command)

        command = "npm install {}".format(package2)
        file_methods.run_command(path,command)

        command = "npm install {}".format(package3)
        file_methods.run_command(path,command)

        command = "npm install {}".format(package4)
        file_methods.run_command(path,command)

        command = "npm install {}".format(package5)
        file_methods.run_command(path,command)
    except Exception as e:
        print(f"Error: {e}")
