import { all } from 'redux-saga/effects';

import appWatchers from './app_sagas';

export default function* rootSaga() {
	const allWatchers = [].concat(
		appWatchers(),
	)
	yield all(allWatchers);
}