import types from '~/redux/types';

const appInitialState = {
	apiToken: undefined,
};

const appState = (state = appInitialState, action) => {
	switch (action.type) {
		case types.SET_API_TOKEN:
			return Object.assign({}, state, {
				apiToken: action.payload.apiToken,
			});
		default:
			return state;
	}
};

export default appState;
