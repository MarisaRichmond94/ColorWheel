import types from '~/redux/types';

const setApiToken = payload => ({
	type: types.SET_API_TOKEN,
	payload: {
		apiToken: payload.apiToken,
	},
});

export default function appActions() {
	return {
		setApiToken,
	}
}
