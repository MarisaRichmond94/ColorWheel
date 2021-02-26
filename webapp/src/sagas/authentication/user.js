import { call, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import types from '~/redux/types';

export function * authenticateUser(action) {
  try {
    const authResults = yield call(AuthenticationApi.post, action.payload);
    yield put({
      type: types.HANDLE_AUTH_RESULTS,
      payload: { authResults },
    });
    const path = `/workspace${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`;
    yield call(window.historyReplace, path);
  } catch (error) {
    const authenticationErrorMessage = (action.payload.name)
      ? 'Account creation failed: There is already an account associated with this email.'
      : 'Login failed: Incorrect email or password.';
    yield put({
      type: types.SET_AUTHENTICATION_ERROR_MESSAGE,
      payload: { authenticationErrorMessage },
    });
  }
}

export function * watchAuthenticateUser() {
  yield takeLatest(types.AUTHENTICATE_USER, authenticateUser);
}
