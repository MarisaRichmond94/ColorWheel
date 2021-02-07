import { fork } from 'redux-saga/effects';

import * as session from './session';
import * as user from './user';

export default function authenticationWatchers() {
  return [
    session.watchAuthenticateSession,
    user.watchAuthenticateUser,
    user.watchDeauthenticateUser,
  ].map(fork);
}
