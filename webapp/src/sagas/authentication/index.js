import { fork } from 'redux-saga/effects';

import * as logoutWarningModal from './logoutWarningModal';
import * as session from './session';
import * as user from './user';

export default function authenticationWatchers() {
  return [
    logoutWarningModal.watchSetIsLogoutWarningModalShowing,
    session.watchAuthenticateSession,
    user.watchAuthenticateUser,
    user.watchDeuthenticateUser,
  ].map(fork);
}
