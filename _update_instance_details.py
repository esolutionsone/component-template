import os
import json

# Specify the root directory and the old_scope_name you want to match
scope_name     = '853443' # old_scope_name from our original working file
component_name = 'component-template'
#Files & Directories to scrub/replace (windows & mac paths below)
mac_files           = [ './now-ui.json','./src/index.js','./src/x-853443-component-template/index.js','./src/x-853443-component-template/__tests__/test.x-853443-component-template.js','./README.md','./example/element.js','./package.json','./package-lock.json' ]
mac_dirs_and_files  = [ './src/x-853443-component-template/__tests__/test.x-853443-component-template.js','./src/x-853443-component-template' ]
win_files           = [ '.\\now-ui.json','.\\src\\index.js','.\\src\\x-853443-component-template\\index.js','.\\src\\x-853443-component-template\\__tests__\\test.x-853443-component-template.js','.\\README.md','.\\example\\element.js','.\\package.json','.\\package-lock.json' ]
win_dirs_and_files  = [ '.\\src\\x-853443-component-template\\__tests__\\test.x-853443-component-template.js','.\\src\\x-853443-component-template' ]
#Utility Functions
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def replace_old_scope_name_in_file(files, old_scope_name, new_scope_name):
    #For each file, read the file in binary mode and replace all instances of the old_scope_name with the new old_scope_name
    for file_path in files:
        with open(file_path, 'rb') as file:  # Open the file in binary mode
            content = file.read() #read the file and encode in utf-8
        if old_scope_name.encode('utf-8') in content:
            updated_content = content.replace(old_scope_name.encode('utf-8'), new_scope_name.encode('utf-8')) #replace all instances of old instance scope

            with open(file_path, 'wb') as file:  # Open the file in binary mode
                file.write(updated_content) # update file with new contents
                print("File cleanup run for {file_path}") # Print impacted files to the terminal
def rename_dirs_and_files(paths, old_scope_name, new_scope_name):
    for path in paths:
        if old_scope_name in path:
            # Only replace last instance of old_scope_name so files get renamed, then dirs on their own loop
            path_list = path.rsplit(old_scope_name, 1)
            new_path  = new_scope_name.join(path_list)
            os.rename(path, new_path) # Update the name of the file or directory
            print("Renamed {path} to {new_path}") # Print impacted file or dir with new path to terminal
def validate_input(value, element):
    if value == "":
            prRed("Please enter a {element}, an empty string is invalid")
    elif " " in value:
        prRed("Invalid, {element} should not contain a space") 
    elif "/" in value:
        prRed("Invalid, {element} should not contain /")
    elif  "\\" in value:
        prRed("Invalid, {element} should not contain \\)")
    else:
        return True
    return False
def run_cleanup(files,dirs,this_file):
    #replace scope in all files but this one & then update directory names
    replace_old_scope_name_in_file(files, scope_name, new_scope_name)
    #replace scope in this file & component if it has been updated
    if new_component_name != '':
        replace_old_scope_name_in_file(files, component_name, new_component_name)

        rename_dirs_and_files(dirs, scope_name+'-'+component_name, new_scope_name+'-'+new_component_name)
    else:
        rename_dirs_and_files(dirs, scope_name+'-'+component_name, new_scope_name+'-'+component_name)
    update_this_file(this_file)
def update_this_file(this_file):
    replace_old_scope_name_in_file([this_file], scope_name, new_scope_name)
    if new_component_name != "":
        replace_old_scope_name_in_file([this_file], component_name, new_component_name)
def cleanup_component_name(scope,component):
    cleanup_comp_scope_name = ("x_"+scope+"_"+component).replace('-','_')[:18]
    if cleanup_comp_scope_name[-1] == '_':
            cleanup_comp_scope_name = cleanup_comp_scope_name[:-1]
    return cleanup_comp_scope_name
def update_now_ui_component_scope(filepath,update_scope_name):
    #Update component scope name in now_ui json file
    with open(filepath) as file:
        json_data = json.load(file)
    json_data['scopeName'] = update_scope_name
    with open(filepath, 'w') as file:
        json.dump(json_data, file, indent=4)
#Renaming logic, user input, validation checking, etc. runs below 
if __name__ == "__main__":
    #Intro Message
    prGreen("\nCurrent appcreator copmany code: x-" + scope_name + "-")
    prLightPurple("\nThis can be found by navigating to \"sys_properties.list\" in the filter navigator of your ServiceNow instance and searching for the property named \"glide.appcreator.company.code\".")
    prLightPurple("\nFor a developer instance, this will likely be a string of numbers! If you're using an organizational instance, it will most likely be a shorthand for your company (for example, ours is esg). \n\nIf you can't find your copmany code, you can try to deploy the component and an error should show the company code.\nFor example, here's an example of the error when deploying to the wrong Personal Developer Instance\n\"ERROR in Component tag name \"x-<scopename>-component-template\" must start with the vendor prefix \"x-853443-\" \nIn this case, 853443 would be the code you enter for scope name!\n")

    #Get new appcreator company code & run check to ensure it is valid
    input_valid = False
    new_scope_name = ''
    while input_valid == False:
        new_scope_name = input("Enter your appcreator company code: ").strip()  # User Input to get new instance scope Use raw_input() in Python 2
        input_valid = validate_input(new_scope_name, "appcreator company code")
    print("\n")

    #Check if the user wants to change the component name (likely most used for converting template to new purpose built component)
    new_component_name       = ''
    component_scope_name     = ''
    new_component_name_valid = False
    change_component_name = input("Do you need to change the component name (current component name "+component_name+"? (y,n):")
    if change_component_name.lower() == 'y' or change_component_name.lower() == 'yes':
        while new_component_name_valid == False:
            new_component_name_ok = ''
            new_component_name = input("please enter your new component name (it is the text after your appcreator company code in the directory within src \nex. x-853443-component-template >> component-template is the component name): ")
            new_component_name_valid = validate_input(new_component_name, "component name")
            if new_component_name_valid != False:
                component_scope_name = cleanup_component_name(new_scope_name,new_component_name)
                new_component_name_ok = input("\nYour New Component Name is " + new_component_name + " and the component scope will be " + component_scope_name + "\nIs this ok? (y,n):")
                if new_component_name_ok.lower() == 'y' or new_component_name_ok.lower() == 'yes':
                    new_component_name_valid = True
                else:
                    new_component_name_valid = False
                print("\n")
    else:
        component_scope_name = cleanup_component_name(new_scope_name,component_name)

    #update now-ui.json component application scope name to be created in ServiceNow
    if os.name == 'posix': 
        update_now_ui_component_scope('./now-ui.json',component_scope_name)
    elif os.name == 'nt':
        update_now_ui_component_scope('.\\now-ui.json',component_scope_name)

    #Get current directory & let user know we're running the script from that dir
    path = os.path.dirname(os.path.abspath(__file__))
    current_directory = os.path.basename(path)
    os.chdir(path)
    print("Running update instance details script from directory: ${current_directory}")
    print(os.path.abspath(__file__))

    #Mac vs. Windows File Structure Handler
    if  os.name == 'posix':
        run_cleanup(mac_files,mac_dirs_and_files,'./_update_instance_details.py')
    elif os.name == 'nt':
        run_cleanup(win_files,win_dirs_and_files,'.\\_update_instance_details.py')

    #If component name is changed, update the main directory (will have to close and reopen component in vscode)
    if new_component_name != '':
        cur_dir = os.getcwd()
        par_dir = os.path.dirname(cur_dir)
        new_directory_path = os.path.join(par_dir, new_component_name)
        if  os.name == 'posix':
            os.rename(cur_dir, new_directory_path)
            prGreen('Renamed directory ${cur_dir} to ${new_component_name} > If you have this open in an editor please close and reopen the new directory!')
        elif os.name == 'nt':
            prGreen('Unable to rename locked folder ${cur_dir} > If you would like to rename this folder, please manually update!')

    prGreen("\nCleanup Complete!\n")