import { all, fork } from 'redux-saga/effects';

import * as authentication from './app_sagas/authentication';

export default function* rootSaga() {
	yield all([
		authentication.watchAuthenticate,
		authentication.watchDeauthenticate,
	].map(fork));
}