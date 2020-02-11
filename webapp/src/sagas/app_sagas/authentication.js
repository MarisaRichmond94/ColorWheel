import { call, put, takeLatest } from 'redux-saga/effects';

import authenticationApi from '~/api/authentication';
import types from '~/redux/types';

function* authenticate(action) {
	const passcode = window.idx(action, _ => _.payload.passcode);
	if (passcode) {
		const apiToken = yield call(authenticationApi.authenticate, passcode);
		if (apiToken && !apiToken.message) {
			yield put({ type: 'SET_API_TOKEN', payload: { apiToken } });
		}
	}
}

function* deauthenticate(action) {
	yield put({ type: 'SET_API_TOKEN', payload: { apiToken: undefined } });
	window.historyReplace('/login');
}

export function* watchAuthenticate() {
	yield takeLatest(types.AUTHENTICATE_USER, authenticate);
}

export function* watchDeauthenticate() {
	yield takeLatest(types.DEAUTHENTICATE_USER, deauthenticate);
}
