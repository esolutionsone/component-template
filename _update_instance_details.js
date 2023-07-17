const fs = require('fs-extra');
const path = require('path');
const readlineSync = require('readline-sync');
const os = require('os');


// Specify the root directory and the old_scope_name you want to match
const scope_name = '853443'; // old_scope_name from our original working file
const component_name = 'component-template';

// Files & Directories to scrub/replace
const files = [
	'./now-ui.json',
	'./src/index.js',
	'./src/x-853443-component-template/index.js',
	'./src/x-853443-component-template/__tests__/test.x-853443-component-template.js',
	'./README.md',
	'./example/element.js',
	'./package.json',
	'./package-lock.json'
];
const dirsAndFiles = [
	'./src/x-853443-component-template/__tests__/test.x-853443-component-template.js',
    './src/x-853443-component-template'
];

// Utility Functions
function prGreen(skk) { console.log("\x1b[92m%s\x1b[00m", skk); }
function prLightPurple(skk) { console.log("\x1b[94m%s\x1b[00m", skk); }
function prRed(skk) { console.log("\x1b[91m%s\x1b[00m", skk); }
function replaceOldScopeNameInFile(files, oldScopeName, newScopeName) {
    //For each file, read the file in binary mode and replace all instances of the old_scope_name with the new old_scope_name
    for (const filePath of files) {
        const content = fs.readFileSync(filePath, 'utf-8');
        if (content.includes(oldScopeName)) {
            const updatedContent = content.replace(new RegExp(oldScopeName, 'g'), newScopeName);
            fs.writeFileSync(filePath, updatedContent, 'utf-8');
            console.log(`File cleanup run for ${filePath}`);
        }
    }
}
function renameDirsAndFiles(paths, oldScopeName, newScopeName) {
    //Only replace last instance of old_scope_name so files get renamed, then dirs on their own loop
    for (const filePath of paths) {
        const last_scope_instance_in_path = new RegExp(`${oldScopeName}(?!.*${oldScopeName})`);
        if (filePath.includes(oldScopeName)) {
            const newFilePath = filePath.replace(last_scope_instance_in_path, newScopeName);
            fs.renameSync(filePath, newFilePath);
            console.log(`Renamed ${filePath} to ${newFilePath}`);
        }
    }
}
function validateInput(value, element) {
    if (value === "") { prRed(`Please enter a ${element}, an empty string is invalid`); } 
    else if (value.includes(" ")) { prRed(`Invalid, ${element} should not contain a space`); } 
    else if (value.includes("/")) { prRed(`Invalid, ${element} should not contain /`); } 
    else if (value.includes("\\")) { prRed(`Invalid, ${element} should not contain \\`); } 
    else { return true; }
    return false;
}
function runCleanup(files, dirs, thisFile, new_scope_name, new_component_name, component_name) {
    //replace scope in all files but this one & then update directory names
    replaceOldScopeNameInFile(files, scope_name, new_scope_name);
    //replace scope in this file & component if it has been updated
    if (new_component_name !== '') {
        replaceOldScopeNameInFile(files, component_name, new_component_name);
        renameDirsAndFiles(dirs, `${scope_name}-${component_name}`, `${new_scope_name}-${new_component_name}`);
    } 
    else { 
        renameDirsAndFiles(dirs, `${scope_name}-${component_name}`, `${new_scope_name}-${component_name}`); 
    }
    updateThisFile(thisFile,new_scope_name,new_component_name)
}
function updateThisFile(thisFile,new_scope_name,new_component_name){
    replaceOldScopeNameInFile([thisFile], scope_name, new_scope_name);
    if (new_component_name !== '') {
        replaceOldScopeNameInFile([thisFile], component_name, new_component_name);
    }
}
function cleanupComponentName(scope, component) {
    let cleanupCompScopeName = `x_${scope}_${component}`.replace(/-/g, '_').slice(0, 18);
    if (cleanupCompScopeName.endsWith('_')) {
        cleanupCompScopeName = cleanupCompScopeName.slice(0, -1);
    }
    return cleanupCompScopeName;
}
function updateNowUIComponentScope(filepath, updateScopeName) {
    //Update component scope name in now_ui json file
    const jsonContent = fs.readFileSync(filepath, 'utf-8');
    const jsonData = JSON.parse(jsonContent);
    jsonData.scopeName = updateScopeName;
    fs.writeFileSync(filepath, JSON.stringify(jsonData, null, 4), 'utf-8');
}
// Renaming logic, user input, validation checking, etc.
if (require.main === module) {
    prGreen(`\nCurrent appcreator company code: x-${scope_name}-`);
    prLightPurple(`\nThis can be found by navigating to "sys_properties.list" in the filter navigator of your ServiceNow instance and searching for the property named "glide.appcreator.company.code".`);
    prLightPurple(`\nFor a developer instance, this will likely be a string of numbers! If you're using an organizational instance, it will most likely be a shorthand for your company (for example, ours is esg).\n\nIf you can't find your company code, you can try to deploy the component and an error should show the company code.\nFor example, here's an example of the error when deploying to the wrong Personal Developer Instance\n"ERROR in Component tag name "x-<scopename>-component-template" must start with the vendor prefix "x-853443-"\nIn this case, 853443 would be the code you enter for scope name!\n`);

    let inputValid = false;
    let new_scope_name = '';
    while (!inputValid) {
        new_scope_name = readlineSync.question('Enter your appcreator company code: ').trim();
        inputValid = validateInput(new_scope_name, 'appcreator company code');
    }
    console.log('\n');

    let new_component_name = '';
    let component_scope_name = '';
    let newComponentNameValid = false;
    const change_component_name = readlineSync.question(`Do you need to change the component name (current component name ${component_name}? (y/n):`);
    if (change_component_name.toLowerCase() === 'y' || change_component_name.toLowerCase() === 'yes') {
        while (!newComponentNameValid) {
            let newComponentNameOk = '';
            new_component_name = readlineSync.question('Please enter your new component name (it is the text after your appcreator company code in the directory within src \nex. x-853443-component-template >> component-template is the component name): ');
            newComponentNameValid = validateInput(new_component_name, 'component name');
            if (newComponentNameValid) {
                component_scope_name = cleanupComponentName(new_scope_name, new_component_name);
                newComponentNameOk = readlineSync.question(`\nYour New Component Name is ${new_component_name} and the component scope will be ${component_scope_name}\nIs this ok? (y/n):`);
                if (newComponentNameOk.toLowerCase() === 'y' || newComponentNameOk.toLowerCase() === 'yes') {
                    newComponentNameValid = true;
                } 
                else {
                    newComponentNameValid = false;
                }
            console.log('\n');
            }
        }
    } 
    else {
        component_scope_name = cleanupComponentName(new_scope_name, component_name);
    }

    if (os.platform() === 'darwin') {
        updateNowUIComponentScope('./now-ui.json', component_scope_name);
    }
    else if (os.platform() === 'win32') {
        updateNowUIComponentScope('.\\now-ui.json', component_scope_name);
    }

    const currentDirectory = path.basename(__dirname);
    console.log(`Running update instance details script from directory: ${currentDirectory}`);

    if (os.platform() === 'darwin') {
        runCleanup(files, dirsAndFiles, './_update_instance_details.js',new_scope_name,new_component_name,component_name);
    }
    else if (os.platform() === 'win32') {
        runCleanup(files, dirsAndFiles, '.\\_update_instance_details.js',new_scope_name,new_component_name,component_name);
    }

    if (new_component_name !== '') {
        const cur_dir = process.cwd();
        const par_dir = path.dirname(cur_dir);
        const new_directory_path = path.join(par_dir, new_component_name);
        if (os.platform() == 'win32'){
            prGreen(`Unable to rename locked folder ${cur_dir} > If you would like to rename this folder, please manually update!`)
        }
        else if (os.platform == 'darwin'){
            fs.renameSync(cur_dir, new_directory_path);
            prGreen(`Renamed directory ${cur_dir} to ${new_component_name} > If you have this open in an editor please close and reopen the new directory!`)
        }
    }

    prGreen('\nCleanup Complete!\n');
}