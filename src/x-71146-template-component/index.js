/* Default imports for UI Builder Components */
import {createCustomElement}  from '@servicenow/ui-core';
import snabbdom               from '@servicenow/ui-renderer-snabbdom';
import styles                 from './styles.scss';
import { UserGreeting } 	  from './components/UserGreeting';
import { LoadingIcon } 		  from './components/LoadingIcon/LoadingIcon';
import actionHandlers         from './actionHandlers';

const view = (state, { updateState, dispatch }) => {
	const { loading, user, method } = state;
	const { title } = state.properties;
	
	if (user === null){
		return <LoadingIcon style={{ transform: 'scale(.5)', backgroundColor: 'white' }}/>;
	}
	return (
		<div>
			{ loading 	?
							<LoadingIcon style={{transform: 'scale(.5)', backgroundColor: backgroundColor}}/>
						:
							<div>
								<h1>{ title }</h1>
								<UserGreeting state={state} />
							</div>
			}
		{/* JSX Switch Statement using Object Literal example */
			{
				"GET": 		<div>Render OPTION1</div>,
				"OPTION2": 	<div>Render OPTION2</div>
			}[method]
		}
		</div>
	);
};

createCustomElement('x-71146-testing-project', {
	renderer: {type: snabbdom},
	/* State variables loading, method, selectedTable, query, and user are included 
	to help with setting up GET / POST but may not be required for your project */
	initialState: {
		loading:			  true,
		method:         	  'GET',
		selectedTable: 	  	  '',
		query:          	  '',
		user:           	  null,
	},
	properties: {
		title:	{ default: "Component REST API Explorer Testing:" },
	},
	view,
	styles,
	actionHandlers
});