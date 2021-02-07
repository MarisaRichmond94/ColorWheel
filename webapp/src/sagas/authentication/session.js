import { all, call, fork, put, takeLatest } from 'redux-saga/effects';

import AuthenticationApi from '~/api/authentication';
import types from '~/redux/types';

function* storeResult(type, payload) {
  yield put({ type, payload });
  const key = Object.keys(payload)[0];
  document.cookie = `${key}=${payload[key]}; max-age=36000;`;
}

export function* storeAuthResultsInSession(authResult) {
  const { email, name, sub: id } = authResult;
  yield all([
    call(storeResult, types.SET_USER_EMAIL, { email }),
    call(storeResult, types.SET_USER_NAME, { name }),
    call(storeResult, types.SET_USER_ID, { id }),
  ]);
}

export function* authenticateSession() {
  if (document.cookie !== '') {
    const authResults = {};

    const keys = ['email', 'id', 'name'];
    keys.forEach(key => {
      authResults[key] = document.cookie.split(';').filter(
        item => keys.includes(item.split('=')[0])
      )[0].split('=')[1];
    });

    if (Object.keys(authResults).length === keys.length) {
      yield all([
        call(storeResult, types.SET_USER_EMAIL, { email: authResults.email }),
        call(storeResult, types.SET_USER_NAME, { name: authResults.name }),
        call(storeResult, types.SET_USER_ID, { id: authResults.id }),
      ]);
      yield fork(refreshSession, authResults.email);
    } else {
      const path = `/login${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`;
      yield call(window.historyReplace, path);
    }
  } else if (window.location.pathname !== '/login') {
    const path = `/login${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`;
    yield call(window.historyReplace, path);
  }
}

export function* refreshSession(email) {
  const authResults = yield call(AuthenticationApi.get, email);
  if (authResults.accessToken) {
    yield put({
      type: types.SET_ACCESS_TOKEN,
      payload: { accessToken: authResults.accessToken },
    });
  }
}

export function* watchAuthenticateSession() {
  yield takeLatest(types.AUTHENTICATE_SESSION, authenticateSession);
}
