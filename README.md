Component Template
===============================================

## Intro
The purpose of this component is to provide a template to start from on your custom component projects 
**The component-template is a simplified/baseline of the REST-API-EXPLORER example component we created** [here](https://github.com/esolutionsone/REST-API-Explorer-Example)
It contains a few boiler plate REST examples, a loading spinner, and a file scrubber so you can rename the component, & update the component with your organizational app code.
 
---

- [Intro](#intro)
- [How to use this Component](#how-to-use-this-component) 
- [What's in the Template?](#what's-in-the-template) 

---

## How to use this component
1) Ensure your sn-cli is configured/installed correctly 
    -> You can review our [Mac OS](https://creator-dna.com/blog/macos-setup) & [Windows OS](https://creator-dna.com/blog/1hj866nlrwslzlesekt0c14grhh8u1) instillation guides
1) Clone this repository `git clone https://github.com/esolutionsone/component-template.git` (to the folder you want to work out of locally)
2) CD to the "component-template" directory
3) Run `npm install`

**To run/use this component locally**

4) Run the renamer script to update your company app creator code and the component name

5) Navigate to [http://localhost:8081/](http://localhost:8081/)

    *Any updates/changes you make to your files locally will be reflected in real-time here!* 🙌

6) Start developing!

**To deploy this component for use in your ServiceNow instance**

1) Run `snc ui-component deploy`
2) Navigate to *UI Builder* in your *ServiceNow Instance* (Now Experience Framework > UI Builder)
3) Click on the experience you'd like to add the component to OR create an experience with the Portal App Shell
4) Create a new UI Builder Page (or open an existing page to add the component to)
5) Search for `<update with component name>` in the Components List, Drag and Drop it onto the page, and click save!

**Voilà, your component is deployed to your ServiceNow instance!**

*(If you make changes to your component down the road, you'll have to redeploy. In our experience this always requires you force deploy your changes.)*


**Assumptions**

    - now-cli config is setup / configured
    - You have an instance to leverage (developer, demo, or organizational sandbox)
    - You know (at a high level) how to read "react-ish" code and how to think "react-ively"
    - You have some experience with UI Builder config
    - Your now-cli profile is pointed at your desired instance for testing this component out!
---

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
