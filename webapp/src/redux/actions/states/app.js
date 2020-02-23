import types from '~/redux/types';

const setIsAuthenticated = payload => ({
	type: types.SET_IS_AUTHENTICATED,
	payload: {
		isAuthenticated: payload.isAuthenticated,
	},
});

export default function appActions() {
	return {
		setIsAuthenticated,
	}
}
