import { fork } from 'redux-saga/effects';

import * as user from './user';

export default function authenticationWatchers() {
  return [
    user.watchAuthenticateUser,
  ].map(fork);
}
