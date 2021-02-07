import { call, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import types from '~/redux/types';
import { storeAuthResultsInSession } from '~/sagas/authentication/session';

export function* authenticateUser(action) {
  const { accessToken, authResults } = yield call(AuthenticationApi.post, action.payload);
  yield put({
    type: types.SET_ACCESS_TOKEN,
    payload: { accessToken },
  });
  yield call(storeAuthResultsInSession, authResults);
  yield call(window.historyReplace, '/');
}

export function* watchAuthenticateUser() {
  yield takeLatest(types.AUTHENTICATE_USER, authenticateUser);
}
