import { call, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import { deauthenticate, setAuthMessage, update } from '~/reducers/user';
import types from '~/sagas/types';

export function * authenticateUser(action) {
  try {
    const authResults = yield call(AuthenticationApi.post, action.payload);
    yield put(update(authResults));
    const path = `/workspace${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`;
    yield call(window.historyReplace, path);
  } catch (error) {
    const authMessage = (action.payload.name)
      ? 'Account creation failed: There is already an account associated with this email.'
      : 'Login failed: Incorrect email or password.';
    yield put(setAuthMessage(authMessage));
  }
}

export function * deauthenticateUser() {
  const cookieKeys = ['email', 'name', 'id'];
  cookieKeys.forEach(key => { document.cookie = `${key}=;max-age=0`; });
  localStorage.clear();
  const path = `/${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`;
  window.historyReplace(path);
  yield put(deauthenticate());
}

export function * watchAuthenticateUser() {
  yield takeLatest(types.AUTHENTICATE_USER, authenticateUser);
}

export function * watchDeuthenticateUser() {
  yield takeLatest(types.DEAUTHENTICATE_USER, deauthenticateUser);
}
