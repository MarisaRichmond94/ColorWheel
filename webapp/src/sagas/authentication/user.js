import { call, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import types from '~/redux/types';

export function* authenticateNewUser(action) {
  const { name, email, password } = action.payload;
  if (name && email && password) {
    const response = yield call(AuthenticationApi.post, name, email, password);
    console.log({ response });
  }
  yield put({ type: types.SET_IS_USER_AUTHENTICATED, payload: { isUserAuthenticated: false } });
}

export function* authenticateUser() {
  // implement authentication later
  yield put({ type: types.SET_IS_USER_AUTHENTICATED, payload: { isUserAuthenticated: false } });
}

export function* watchAuthenticateNewUser() {
  yield takeLatest(types.AUTHENTICATE_NEW_USER, authenticateNewUser);
}

export function* watchAuthenticateUser() {
  yield takeLatest(types.AUTHENTICATE_USER, authenticateUser);
}
