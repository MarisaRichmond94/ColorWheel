import { call, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import types from '~/redux/types';
import { storeAuthResultsInSession } from '~/sagas/authentication/session';

export function * authenticateUser(action) {
  try {
    const { accessToken, authResults } = yield call(AuthenticationApi.post, action.payload);
    yield put({
      type: types.SET_ACCESS_TOKEN,
      payload: { accessToken },
    });
    yield call(storeAuthResultsInSession, authResults);
    yield call(window.historyReplace, '/home');
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
