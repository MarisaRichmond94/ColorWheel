import { call, fork, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import { setIsAuthenticating, update } from '~/reducers/user';
import types from '~/sagas/types';

export function * authenticateSession() {
  if (document.cookie !== '') {
    const authResults = {};

    const keys = ['email', 'id', 'name'];
    keys.forEach(key => {
      authResults[key] = document.cookie.split(';').filter(
        item => item.split('=')[0].includes(key),
      )[0].split('=')[1];
    });

    if (Object.keys(authResults).length === keys.length) {
      yield fork(refreshSession, authResults.email);
    } else {
      yield fork(routeBackToLogin);
    }
  } else {
    yield fork(routeBackToLogin);
  }
}

function * routeBackToLogin() {
  yield put(setIsAuthenticating(false));
  const path = `/${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`;
  yield call(window.historyReplace, path);
}

export function * refreshSession(email) {
  const authResults = yield call([AuthenticationApi, AuthenticationApi.get], email);
  yield put(update(authResults));
  yield put(setIsAuthenticating(false));
}

export function * watchAuthenticateSession() {
  yield takeLatest(types.AUTHENTICATE_SESSION, authenticateSession);
}
