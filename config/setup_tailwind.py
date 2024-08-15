import utils.file_methods as file_methods
import constants.input_label as input_label

package1 = "npm i tailwindcss postcss autoprefixer"
package2 = "npx tailwindcss init"

def main(path):

    try:


        src_path = "{}/{}".format(path,"src")

        # Install Redux
        install_tailwind(path)

        # Setup Redux
        from_source = "components/tailwind"
        file = "index.css"
        file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(src_path,file))

        from_source = "components/tailwind"
        file = "postcss.config.js"
        file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(path,file))
        from_source = "components/tailwind"
        file = "tailwind.config.js"
        file_methods.copy_paste_file("{}/{}".format(from_source,file),"{}/{}".format(path,file))
    
    except Exception as e:
        print(f"Error: {e}")
    
def install_tailwind(path):
    try:
        file_methods.run_command(path,package1)

        file_methods.run_command(path,package2)
    except Exception as e:
        print(f"Error: {e}")
