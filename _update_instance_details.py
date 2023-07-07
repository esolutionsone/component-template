import os

def replace_old_scope_name_in_file(files, old_scope_name, new_scope_name):
    #For each file, read the file in binary mode and replace all instances of the old_scope_name with the new old_scope_name
    for file_path in files:
        with open(file_path, 'rb') as file:  # Open the file in binary mode
            content = file.read() #read the file and encode in utf-8
        if old_scope_name.encode('utf-8') in content:
            updated_content = content.replace(old_scope_name.encode('utf-8'), new_scope_name.encode('utf-8')) #replace all instances of old instance scope

            with open(file_path, 'wb') as file:  # Open the file in binary mode
                file.write(updated_content) # update file with new contents
                print(f"File cleanup run for {file_path}") # Print impacted files to the terminal

def rename_dirs_and_files(paths, old_scope_name, new_scope_name):
    for path in paths:
        if old_scope_name in path:
            # Only replace last instance of old_scope_name so files get renamed, then dirs on their own loop
            path_list = path.rsplit(old_scope_name, 1)
            new_path  = new_scope_name.join(path_list)
            os.rename(path, new_path) # Update the name of the file or directory
            print(f"Renamed {path} to {new_path}") # Print impacted file or dir with new path to terminal
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

# Specify the root directory and the old_scope_name you want to match
scope_name     = '853443' # old_scope_name from our original working file
component_name = 'template-component'
prGreen("\nCurrent appcreator copmany code: x-" + scope_name + "-")
prLightPurple("\nThis can be found by navigating to \"sys_properties.list\" in the filter navigator of your ServiceNow instance and searching for the property named \"glide.appcreator.company.code\".")
prLightPurple("\nFor a developer instance, this will likely be a string of numbers! If you're using an organizational instance, it will most likely be a shorthand for your company (for example, ours is esg). \n\nIf you can't find your copmany code, you can try to deploy the component and an error should show the company code.\nFor example, here's an example of the error when deploying to the wrong Personal Developer Instance\n\"ERROR in Component tag name \"x-<scopename>-template-component\" \nmust start with the vendor prefix \"x-853443-\" \nIn this case, 853443 would be the code you enter for scope name!\n")

#Run check to ensure appcreator company code is valid
input_valid = False
new_scope_name = ''
while input_valid == False:
    new_scope_name = input("Enter your appcreator company code: ").strip()  # User Input to get new instance scope Use raw_input() in Python 2
    if new_scope_name == "":
        prRed("Please enter an appcreator copmany code, an empty string is invalid")
    elif "/" in new_scope_name:
        prRed("Invalid appcreator copmany code, please enter a valid company code (should not contain /)")
    elif  "\\" in new_scope_name:
        prRed("Invalid appcreator copmany code, please enter a valid company code (should not contain \\)")
    else:
        input_valid = True
print("\n")

change_component_name = input("Do you need to change the component name (current component name "+component_name+"? (y,n):")
if change_component_name.lower() == 'y' or change_component_name.lower() == 'yes':
    new_component_name_valid = False
    while new_component_name_valid == False:
        new_component_name = input("please enter your new component name (it is the text after your appcreator company code in the directory within src ex. x-853443-template-component >> template-component is the component name)")
        if new_component_name == "":
            prRed("Please enter component name, an empty string is invalid")
        elif "/" in new_component_name:
            prRed("Invalid component name, please enter a valid company code (should not contain /)")
        elif  "\\" in new_component_name:
            prRed("Invalid component name, please enter a valid company code (should not contain \\)")
        else:
            input_valid = True
        print("\n")

    if  os.name == 'posix':
        replace_old_scope_name_in_file(['./_update_instance_details.py'], component_name, new_component_name)
    elif os.name == 'nt':
        replace_old_scope_name_in_file(['./_update_instance_details.py'], component_name, new_component_name)
    prGreen('Updated component name in _update_instance_details.py file! \n')
# Call functions to replace scope old_scope_namees in file contents & to rename directories, & files
# First cleanup file contents, then files, then directories to ensure the no "file not found" errors

#Check if we're in the appropriate directory
#If not, Navigate to the appropriate directory to run the script
#If the above doesn't work, add note to user that we need to be in the correct directory
path = os.path.dirname(os.path.abspath(__file__))
current_directory = os.path.basename(path)
os.chdir(path)
print("Running update instance details script from directory: " + current_directory)

#Files & Directories to scrub/replace (windows & mac paths below)
mac_files           = [ './now-ui.json',
                        './src/index.js',
                        './src/x-853443-template-component/index.js',
                        './src/x-853443-template-component/__tests__/test.x-853443-template-component.js',
                        './README.md',
                        './example/element.js',
                        './_update_instance_details.py' ]
mac_dirs_and_files  = [ './src/x-853443-template-component/__tests__/test.x-853443-template-component.js',
                        './src/x-853443-template-component' ]

win_files           = [ '.\\now-ui.json',
                        '.\\src\\index.js',
                        '.\\src\\x-853443-template-component\\index.js',
                        '.\\src\\x-853443-template-component\\__tests__\\test.x-853443-template-component.js',
                        '.\\README.md',
                        '.\\example\\element.js',
                        '.\\_update_instance_details.py' ]
win_dirs_and_files = [  '.\\src\\x-853443-template-component\\__tests__\\test.x-853443-template-component.js',
                        '.\\src\\x-853443-template-component' ]

# If we're running Linux/Mac based, use mac files, elif we're using Windows, use Windows filepaths
if  os.name == 'posix':
    replace_old_scope_name_in_file(mac_files, scope_name, new_scope_name)
    rename_dirs_and_files(mac_dirs_and_files, scope_name, new_scope_name)
elif os.name == 'nt':
    replace_old_scope_name_in_file(win_files, scope_name, new_scope_name)
    rename_dirs_and_files(win_dirs_and_files, scope_name, new_scope_name)

prGreen("\nCleanup Complete!\n")