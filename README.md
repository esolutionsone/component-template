Component Template
===============================================

## Intro
The purpose of this component is to provide a template to start from on your custom component projects 
**The component-template is a simplified/baseline of the** [REST-API-EXPLORER](https://github.com/esolutionsone/REST-API-Explorer-Example) **example component. We created this component to illustrate how a more complex component could be structured and to show how REST messages could be used to fetch records from and create records in your instance.**
It contains a few boiler plate REST examples, a loading spinner, and a file scrubber so you can rename the component, & update the component with your organizational app code.
 
---

- [Intro](#intro)
- [How to use this Component](#how-to-use-this-component) 
- [What's in the Template?](#what's-in-the-template) 

---

## How to use this component

**Prerequisites**

- sn-cli
- Git
- VSCode (strongly recommended)

**Getting Started**

1) Ensure your sn-cli is configured/installed correctly 
    &rarr; You can review our [Mac OS](https://creator-dna.com/blog/macos-setup) & [Windows OS](https://creator-dna.com/blog/1hj866nlrwslzlesekt0c14grhh8u1) instillation guides
&ensp;
2) Clone this repository `git clone https://github.com/esolutionsone/component-template.git` (to the folder you want to work out of locally)

>**NOTE:** Double check you are in the correct folder before moving on to the next step. "component-template" should be the folder you are in. You can check by looking at your terminal command line to verify.

3) Run `npm install` in your terminal

>**NOTE:** If the **`npm install`** only takes a few seconds, you are most likely in the wrong folder. Change directory **`cd`** into the appropriate folder and retry **`npm install`** command. If you changed into the right folder, you will be waiting a few minutes for all the modules to install.

4) Locate your company code by navigating to `sys_properties.list` in the filter navigator of your ServiceNow instance and searching for the property named `glide.appcreator.company.code`. 

>**NOTE:** For a developer instance, this will likely be a string of numbers! If you're using an organizational instance, it will most likely be a shorthand for your company (for example, ours is esg). 

If you can't find your copmany code, you can try to deploy the component and an error should show the company code. Here's an example of the error when deploying to the wrong Personal Developer Instance:
><span style="color:red"> ERROR in Component tag name "x-853443-testing-project" must start with the vendor prefix "x-71146-"</span>

In this case, 71146 would be the code you enter for scope name!

5) Once you have the company code, run `npm run rename` in your terminal and you will be prompted to enter your scope name. Enter the company code and hit `ENTER` on your keyboard. You will notice a couple files will be updated with the appropriate company code. 


**To run/use this component locally**

6) Run `snc ui-component develop`

>**NOTE:** *You can also use* **`npm run dev`** *as we've created a run dev script in package.json!*
&ensp;
7) Navigate to [http://localhost:8081/](http://localhost:8081/)

>**NOTE:** *Any updates/changes you make to your files locally will be reflected in real-time here!* 🙌

**To deploy this component for use in your ServiceNow instance**

8) Run `snc ui-component deploy`
&ensp;
9) Navigate to *UI Builder* in your *ServiceNow Instance* (Now Experience Framework > UI Builder)
&ensp;
10) Click on the experience you'd like to add the component to OR create an experience with the Portal App Shell
&ensp;
11) Create a new UI Builder Page (or open an existing page to add the component to)
&ensp;
12) Search for `REST API Explorer` in the Components List, Drag and Drop it onto the page, and click save!

**Voilà, your component is deployed to your ServiceNow instance!**

>**NOTE:** *If you make changes to your component down the road, you'll have to redeploy. In our experience this always requires you force deploy your changes.*

**Assumptions**

    - now-cli config is setup / configured
    - You have an instance to leverage (developer, demo, or organizational sandbox)
    - You know (at a high level) how to read "react-ish" code and how to think "react-ively"
    - You have some experience with UI Builder config
    - Your now-cli profile is pointed at your desired instance for testing this component out!

## What's in the Template?

    - Components Folder with LoadingIcon & UserGreeting Components
      - LoadingIcon shows when loading state == true
      - UserGreeting is populated with the current users name
    - actionHandlers.js
      - Bootstrap example fetches logged in user details
      - REST POST & GET examples
    - helpers.js
      - Example REST GET & POST dispatches to the actionHandlers
      - debounce function to be used to limit server calls
    - _update_instance_details >> Component Scrubber / Renamer script
      - Allows you to update the company app creator code & change the component name
