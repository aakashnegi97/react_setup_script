import utils.file_methods as file_methods
import constants.input_label as input_label

package = "react-router-dom"

def main(path):

    try:
        is_created = file_methods.check_dependency(path,package)
        if not is_created:

            src_path = "{}/{}".format(path,"src")
            src_routes_path = "{}/{}".format(src_path,"routes")

            # Install React Route
            install_react_router_dom(path)

            # Setup React Route
            from_source = "components/routes"
            file = "config.js"
            file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(src_routes_path,file))
            file = "index.js"
            file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(src_routes_path,file))
            file = "PrivateRoutes.js"
            file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(src_routes_path,file))
            file = "PublicRoutes.js"
            file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(src_routes_path,file))
            file = "App.js"
            file_methods.copy_paste_file("{}/{}".format("components",file),"{}/{}".format(src_path,file))

            layoutPath = "{}/components/layouts".format(src_path)
            file_methods.make_dir_if_not_exist(layoutPath)

            file = "PublicLayout.js"
            file_methods.copy_paste_file("{}/{}".format("components/layouts",file),"{}/components/layout/{}".format(src_path,file))
            file = "PrivateLayout.js"
            file_methods.copy_paste_file("{}/{}".format("components/layouts",file),"{}/components/layout/{}".format(src_path,file))

        else:
            print(input_label.package_already_setup_message(package))


    except Exception as e:
        print(f"Error: {e}")
    
def install_react_router_dom(path):
    try:
        command = "npm install {}".format(package)
        file_methods.run_command(path,command)
    except Exception as e:
        print(f"Error: {e}")
