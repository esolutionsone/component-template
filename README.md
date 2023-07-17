Component Template
===============================================

## Intro
The purpose of this component is to provide a template to start from on your custom component projects 
**The component-template is a simplified/baseline of the REST-API-EXPLORER example component we created** [here](https://github.com/esolutionsone/REST-API-Explorer-Example)
It contains a few boiler plate REST examples, a loading spinner, and a file scrubber so you can rename the component, & update the component with your organizational app code.

---

- [Intro](#intro)
- [How to use this Component](#how-to-use-this-component)
- [File structure](#file-structure)
- [Components](#components)
    - [Loading Icon](#loading-icon)
    - [User Greeting](#user-greeting)
- [Helpers and ActionHandlers](#helpers-and-actionhandlers)
- [Properties](#properties)

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

## File structure
    - src                            ➜ Source code for our custom component!
        - x-853443-testing-project    ➜ Our Component (all custom code should be in here)
            - tests                  ➜ Component tests 
            - components             ➜ Folder that holds all sub-components
                - LoadingIcon        ➜ Folder containing all LoadingIcon component files
                - User Greeting      ➜ Folder containing all UserGreeting component files
            - actionHandlers.js      ➜ Our actionHandlers handle dispatches and REST calls!
            - helper.js              ➜ Our helper handles function calls in click, change, etc.
            - index.js               ➜ This is our "core component"
            - styles.scss            ➜ This is our core style sheet
        - index.js                   ➜ Wrapper for your custom component (don't touch 😊)
    - now-ui.json                    ➜ Add properties to configure the Component in UI Builder here
    - package.json                   ➜ Can add dependencies & scripts to make dev easier here

---

## Helpers and ActionHandlers


## helpers.js

**sendRest**

    Handles the POST and GET requests and sends the dispatch requests to make REST API requests to your 
    ServiceNow instance. It also handles (simple) form validation and will enforce mandatory fields. 
    This also leverages the debounce function to limit the calls it makes to the server. If the mandatory 
    fields check passes the processREST function will be called. 

**processREST**

    Determines if it is a GET or POST request and sends the appropriate dispatch "REST_GET" or "REST_POST" 
    to the actionHandlers with the required inputs. This function is called by the sendRest function.

**debounce**

    Leveraged by the fetchValues and sendRest functions to limit the calls each function makes to the server. 
    For the fetchValues function it limits the number of lookups as it would continually look up with each 
    keypress and for the sendRest it limits multiple lookups if a user spam clicks the send button. 



## actionHandlers.js
**COMPONENT_BOOTSTRAPPED**

    Calls the GET_USER action when the component is Bootstrapped

**REST_GET**

    Send a REST GET Message leveraging the table api to your ServiceNow instance with the provided arguments. 
    On success, it calls the GET_RESPONSE_VALUE function and on failure, it calls the LOG_ERROR function. 
    Called by the ProcessRest function in helpers. 

**REST_POST**

    Send a REST POST Message leveraging the table API to your ServiceNow instance with the provided arguments 
    and request body. On success, call the POST_RESPONSE_VALUE function. On failure, call the LOG_ERROR function. 
    Called by the ProcessRest function in helpers.  

**GET_USER**

    Send a REST GET Message leveraging the table API to your ServiceNow with the provided arguments to fetch 
    the currently logged-in user. On success, call the SET_USER_ID function. On failure call the LOG_ERROR function. 
    Called by the COMPONENT_BOOTSTRAPPED action.

**GET_RESPONSE_VALE**

    Sets the value of "results" from the REST response value sent in the REST_GET action and sets "loading" 
    to false in state.

**POST_RESPONSE_VALUE**

    Sets the value of "post_response" from the REST response value sent in the REST_POST action and sets 
    "loading" to false in state.

**SET_USER_ID**

    Sets the value of "user" from the REST response value sent in the GET_USER action and sets "loading" to false 
    in state. 

**LOG_ERROR**

    Console logs errors for any actions that encounter issues in processing. Prints the error message and data from 
    the payload. 
    
---

### Properties
Properties can be added to your component to allow for In Platform configuration! In this component, we have a title, background color, body text color, heading text color, hero image url override, table, and query. These values can be configured in UI Builder to change the styling, header text, and default values for the fields.

Properties can be a string, boolean, choice, JSON, or even table/reference select value. Here are a few examples from the ServiceNow Button component and this component for how properties can be set in the now-ui.json file.

*Choice*
```
  {
    "defaultValue": "navigation",
    "description": "Sets the button style",
    "fieldType": "choice",
    "label": "Variant",
    "name": "variant",
    "readOnly": false,
    "required": false,
    "selectable": false,
    "typeMetadata": {
      "choices": [
        {
          "label": "Primary",
          "value": "primary"
        },
        {
          "label": "Navigation",
          "value": "navigation"
        },
        {
          "label": "Add Record",
          "value": "add-record"
        }
      ],
      "schema": {
        "type": "string",
        "enum": ["primary", "navigation", "add-record"]
      }
    }
  }
```

*String*
```
  {
    "defaultValue": "Button",
    "description": "Text displayed inside the button",
    "fieldType": "string",
    "label": "Label",
    "name": "label",
    "readOnly": false,
    "required": true,
    "selectable": false,
    "typeMetadata": {
      "translatable": true,
      "schema": {
        "type": "string"
      }
    }
  }
```

*Boolean*
```
  {
    "defaultValue": false,
    "description": "When true, disables user click interactions",
    "fieldType": "boolean",
    "label": "Disabled",
    "name": "disabled",
    "readOnly": false,
    "required": false,
    "selectable": false,
    "typeMetadata": {
      "schema": {
        "type": "boolean"
      }
    }
  }
```

*Table Lookup*
```
  {
    "name": "table",
    "label": "Table",
    "fieldType": "table_name",
    "readOnly": false,
    "defaultValue": "",
    "description": "Select the table data to display in the list.",
    "selectable": false,
    "valueType": "string",
    "mandatory": true
  }
```
*JSON*
```
  {
    "defaultValue": "{}",
    "description": "Configures ARIA properties",
    "fieldType": "json",
    "label": "ARIA properties",
    "name": "configAria",
    "readOnly": false,
    "required": false,
    "selectable": false,
    "typeMetadata": {
      "schema": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "button": {
                "type": "object",
                "properties": {
                  "aria-braillelabel": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-brailleroledescription": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-colindextext": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-description": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-label": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-placeholder": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-roledescription": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-rowindextext": {
                    "type": "string",
                    "translatable": true
                  },
                  "aria-valuetext": {
                    "type": "string",
                    "translatable": true
                  }
                },
                "patternProperties": {
                  "^aria-": {
                    "type": "string"
                  }
                },
                "additionalProperties": false
              }
            },
            "additionalProperties": false
          },
          {
            "type": "object",
            "properties": {
              "aria-braillelabel": {
                "type": "string",
                "translatable": true
              },
              "aria-brailleroledescription": {
                "type": "string",
                "translatable": true
              },
              "aria-colindextext": {
                "type": "string",
                "translatable": true
              },
              "aria-description": {
                "type": "string",
                "translatable": true
              },
              "aria-label": {
                "type": "string",
                "translatable": true
              },
              "aria-placeholder": {
                "type": "string",
                "translatable": true
              },
              "aria-roledescription": {
                "type": "string",
                "translatable": true
              },
              "aria-rowindextext": {
                "type": "string",
                "translatable": true
              },
              "aria-valuetext": {
                "type": "string",
                "translatable": true
              }
            },
            "patternProperties": {
              "^aria-": {
                "type": "string"
              }
            },
            "additionalProperties": false
          }
        ]
      }
    }
  }
```