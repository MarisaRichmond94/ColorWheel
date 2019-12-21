import { takeLatest } from 'redux-saga/effects';

function authenticate(action) {
	// TODO
}

function deauthenticate(action) {
	// TODO
}

export function* watchAuthenticate() {
	yield takeLatest('LOG_IN', authenticate);
}

export function* watchDeauthenticate() {
	yield takeLatest('LOG_OUT', deauthenticate);
}
