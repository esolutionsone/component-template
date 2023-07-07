/* component that greets the logged in user */

/* In order to access the props("state", "updateState") that were passed down from the parent component(view)
we need to destructure them. */
export const UserGreeting = ({ state }) => {
    /* Next, we destrucure all the variables needed from state and properties*/
    const { user } = state;
    const { headerTextColor } = state.properties;
    /* Render the greeting to the user & dynamically set color based on properties */
    return (
        user != null ?
            <div  style={{ color: headerTextColor }} className="user-greeting">
                <p>Hello, { user[0].name }</p>
            </div>
            :
            ""
    )
}