import types from '~/redux/types';

const appInitialState = {
	isAuthenticated: false,
};

const appState = (state = appInitialState, action) => {
	switch (action.type) {
		case types.SET_IS_AUTHENTICATED:
			return Object.assign({}, state, {
				isAuthenticated: action.payload.isAuthenticated,
			});
		default:
			return state;
	}
};

export default appState;
