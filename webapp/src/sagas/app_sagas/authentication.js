import { call, put, takeLatest } from 'redux-saga/effects';

import authenticationApi from '~/api/authentication';
import types from '~/redux/types';

function* authenticate(action) {
	const passcode = window.idx(action, _ => _.payload.passcode);
	if (passcode) {
		const isAuthenticated = yield call(authenticationApi.authenticate, passcode);
		if (isAuthenticated && !isAuthenticated.message) {
			yield put({ type: 'SET_IS_AUTHENTICATED', payload: { isAuthenticated } });
			window.historyReplace('/');
		}
	}
}

function* rauthenticate(action) {
	const path = window.location.pathname;
	if (path !== '/login') {
		const isAuthenticated = yield call(authenticationApi.reauthenticate);
		yield put({ type: 'SET_IS_AUTHENTICATED', payload: { isAuthenticated } });
		if (!isAuthenticated) {
			window.historyReplace('/login');
		}
	}
}

function* deauthenticate(action) {
	yield put({ type: 'SET_IS_AUTHENTICATED', payload: { isAuthenticated: false } });
	window.historyReplace('/login');
}

export function* watchAuthenticate() {
	yield takeLatest(types.AUTHENTICATE_USER, authenticate);
}

export function* watchReauthenticate() {
	yield takeLatest(types.REAUTHENTICATE_USER, rauthenticate);
}

export function* watchDeauthenticate() {
	yield takeLatest(types.DEAUTHENTICATE_USER, deauthenticate);
}
