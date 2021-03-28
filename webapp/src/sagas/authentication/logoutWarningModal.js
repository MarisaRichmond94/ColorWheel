import { put, takeLatest } from 'redux-saga/effects';

import { setIsLogoutWarningModalShowing } from '~/reducers/user';
import types from '~/sagas/types';

export function * setIsLogoutWarningModalShowingSaga(action) {
  yield put(setIsLogoutWarningModalShowing(action.payload.isLogoutWarningModalShowing));
}

export function * watchSetIsLogoutWarningModalShowing() {
  yield takeLatest(types.SET_IS_LOGOUT_WARNING_MODAL_SHOWING, setIsLogoutWarningModalShowingSaga);
}
