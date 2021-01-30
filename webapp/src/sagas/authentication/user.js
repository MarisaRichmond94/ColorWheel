import { put, takeLatest } from 'redux-saga/effects';

import types from '~/redux/types';

export function* authenticateUser() {
  // implement authentication later
  yield put({ type: types.SET_IS_USER_AUTHENTICATED, payload: { isUserAuthenticated: false } });
}

export function* watchAuthenticateUser() {
  yield takeLatest(types.AUTHENTICATE_USER, authenticateUser);
}