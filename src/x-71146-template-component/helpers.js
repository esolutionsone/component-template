export const sendRest = debounce(( state, dispatch) => {
    processREST( state, dispatch);
})

let processREST = ( state, dispatch ) => {
    const { method, selectedTable, query } = state;
    if ( method === 'GET' ){
        dispatch("REST_GET", {
            tableName:     selectedTable,
            sysparm_query: query
        }) 
    }
    else if ( method === 'POST' ){
        let requestBody = {"short_description":"example body"};
        dispatch("REST_POST", {
            tableName: selectedTable,
            data:      requestBody
        })
    }
}
function debounce(func, timeout = 300){
    /* Call the function passed in after the timer times out >> indended to reduce calls to the server */
    let timer;
    return (...args) => {
        clearTimeout(timer);
        timer = setTimeout(() => { func.apply(this, args); }, timeout);
    };
}