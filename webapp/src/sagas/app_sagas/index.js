import { fork } from 'redux-saga/effects';

import * as authentication from './authentication';

export default function appWatchers() {
	return [
		authentication.watchAuthenticate,
		authentication.watchDeauthenticate,
	].map(fork);
}