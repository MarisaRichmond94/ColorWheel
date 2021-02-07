import { all } from 'redux-saga/effects';

import authenticationWatchers from './authentication';

export default function * rootSaga() {
  const allWatchers = [].concat(
    authenticationWatchers(),
  );

  yield all(allWatchers);
}
