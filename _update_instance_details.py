import os
import json

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
component_name = 'component-template'

prGreen("\nCurrent appcreator copmany code: x-" + scope_name + "-")
prLightPurple("\nThis can be found by navigating to \"sys_properties.list\" in the filter navigator of your ServiceNow instance and searching for the property named \"glide.appcreator.company.code\".")
prLightPurple("\nFor a developer instance, this will likely be a string of numbers! If you're using an organizational instance, it will most likely be a shorthand for your company (for example, ours is esg). \n\nIf you can't find your copmany code, you can try to deploy the component and an error should show the company code.\nFor example, here's an example of the error when deploying to the wrong Personal Developer Instance\n\"ERROR in Component tag name \"x-<scopename>-component-template\" must start with the vendor prefix \"x-853443-\" \nIn this case, 853443 would be the code you enter for scope name!\n")

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
new_component_name       = ''
component_scope_name     = ''
new_component_name_valid = False
change_component_name = input("Do you need to change the component name (current component name "+component_name+"? (y,n):")
if change_component_name.lower() == 'y' or change_component_name.lower() == 'yes':
    while new_component_name_valid == False:
        new_component_name_ok = 'n'
        new_component_name = input("please enter your new component name (it is the text after your appcreator company code in the directory within src \nex. x-853443-component-template >> component-template is the component name): ")
        if new_component_name == "":
            prRed("Please enter component name, an empty string is invalid")
        elif " " in new_component_name:
            prRed("Invalid component name, company code should not contain a space") 
        elif "/" in new_component_name:
            prRed("Invalid component name, company code should not contain /")
        elif  "\\" in new_component_name:
            prRed("Invalid component name, company code should not contain \\)")
        component_scope_name = ("x_"+new_scope_name+"_"+new_component_name).replace('-','_')[:18]
        # Check if the last character is an underscore and strip it if present
        if component_scope_name[-1] == '_':
            component_scope_name = component_scope_name[:-1]
        new_component_name_ok = input("Your New Component Name is " + new_component_name + " and the component scope will be " + component_scope_name + "\nIs this ok? (y,n):")
        if new_component_name_ok.lower() == 'y' or new_component_name_ok.lower() == 'yes':
            new_component_name_valid = True
        print("\n")
else:
    component_scope_name = ("x_"+new_scope_name+"_"+component_name).replace('-','_')[:18]
    if component_scope_name[-1] == '_':
            component_scope_name = component_scope_name[:-1]

now_ui = ''
if os.name == 'posix': 
    now_ui = './now-ui.json'
elif os.name == 'nt':
    now_ui = '.\\now-ui.json'

with open(now_ui) as file:
    json_data = json.load(file)
json_data['scopeName'] = component_scope_name
with open(now_ui, 'w') as file:
    json.dump(json_data, file, indent=4)

#Check if we're in the appropriate directory
#If not, Navigate to the appropriate directory to run the script
#If the above doesn't work, add note to user that we need to be in the correct directory
path = os.path.dirname(os.path.abspath(__file__))
current_directory = os.path.basename(path)
os.chdir(path)
print("Running update instance details script from directory: " + current_directory)
print(os.path.abspath(__file__))
#Files & Directories to scrub/replace (windows & mac paths below)
mac_files           = [ './now-ui.json',
                        './src/index.js',
                        './src/x-853443-component-template/index.js',
                        './src/x-853443-component-template/__tests__/test.x-853443-component-template.js',
                        './README.md',
                        './example/element.js',
                        './package.json',
                        './package-lock.json' ]
mac_dirs_and_files  = [ './src/x-853443-component-template/__tests__/test.x-853443-component-template.js',
                        './src/x-853443-component-template' ]

win_files           = [ '.\\now-ui.json',
                        '.\\src\\index.js',
                        '.\\src\\x-853443-component-template\\index.js',
                        '.\\src\\x-853443-component-template\\__tests__\\test.x-853443-component-template.js',
                        '.\\README.md',
                        '.\\example\\element.js',
                        '.\\package.json',
                        '.\\package-lock.json' ]
win_dirs_and_files = [  '.\\src\\x-853443-component-template\\__tests__\\test.x-853443-component-template.js',
                        '.\\src\\x-853443-component-template' ]

# If we're running Linux/Mac based, use mac files, elif we're using Windows, use Windows filepaths
if  os.name == 'posix':
    #replace scope in all files but this one & then update directory names
    replace_old_scope_name_in_file(mac_files, scope_name, new_scope_name)
    #replace scope in this file & component it it has been updated
    if new_component_name != '':
        replace_old_scope_name_in_file(mac_files, component_name, new_component_name)
        replace_old_scope_name_in_file(['./_update_instance_details.py'], component_name, new_component_name)
        rename_dirs_and_files(mac_dirs_and_files, scope_name+'-'+component_name, new_scope_name+'-'+new_component_name)
    else:
        rename_dirs_and_files(mac_dirs_and_files, scope_name+'-'+component_name, new_scope_name+'-'+component_name)
    replace_old_scope_name_in_file(['./_update_instance_details.py'], scope_name, new_scope_name)
elif os.name == 'nt':
    #replace scope in all files but this one & then update directory names
    replace_old_scope_name_in_file(win_files, scope_name, new_scope_name)
    #replace scope in this file & component it it has been updated
    if new_component_name != '':
        replace_old_scope_name_in_file(win_files, component_name, new_component_name)
        replace_old_scope_name_in_file(['.\\_update_instance_details.py'], component_name, new_component_name)
        rename_dirs_and_files(win_dirs_and_files, scope_name+'-'+component_name, new_scope_name+'-'+new_component_name)
    else:
        rename_dirs_and_files(win_dirs_and_files, scope_name+'-'+component_name, new_scope_name+'-'+component_name)
    replace_old_scope_name_in_file(['.\\_update_instance_details.py'], scope_name, new_scope_name)

if new_component_name != '':
    # Get the current directory path
    cur_dir = os.getcwd()
    # Get the parent directory path
    par_dir = os.path.dirname(cur_dir)
    # Construct the new directory path
    if new_component_name != '':
        new_directory_path = os.path.join(par_dir, new_component_name)
    else:
        new_directory_path = os.path.join(par_dir, component_name)
    # Rename the directory
    os.rename(cur_dir, new_directory_path)
    print(cur_dir,',',par_dir)

prGreen("\nCleanup Complete!\n")