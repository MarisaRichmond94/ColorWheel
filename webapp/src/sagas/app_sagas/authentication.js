import { put, takeLatest } from 'redux-saga/effects';

import types from '~/redux/types';

function* authenticate(action) {
	const passcode = window.idx(action, _ => _.payload.passcode);
	if (passcode) {
		const apiToken = 'aBcD.eFgH.iJkL'; // replace this with an api call
		if (apiToken) {
			yield put({ type: 'SET_API_TOKEN', payload: { apiToken } });
			window.historyReplace('/home');
		}
	}
}

function* deauthenticate(action) {
	yield put({ type: 'SET_API_TOKEN', payload: { apiToken: undefined } });
	window.historyReplace('/');
}

export function* watchAuthenticate() {
	yield takeLatest(types.AUTHENTICATE_USER, authenticate);
}

export function* watchDeauthenticate() {
	yield takeLatest(types.DEAUTHENTICATE_USER, deauthenticate);
}
