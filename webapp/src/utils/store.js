import { configureStore, getDefaultMiddleware } from '@reduxjs/toolkit';
import { routerMiddleware } from 'react-router-redux';
import createSagaMiddleware from 'redux-saga';

import authConfigMiddleware from '~/middleware/authConfig';
import reducer from '~/reducers';
import rootSaga from '~/sagas';
import history from '~/utils/history';

const sagaMiddleware = createSagaMiddleware();

const store = configureStore({
  devTools: process.env.NODE_ENV === 'development',
  reducer,
  middleware: [
    ...getDefaultMiddleware(),
    sagaMiddleware,
    routerMiddleware(history),
    authConfigMiddleware,
  ],
});

sagaMiddleware.run(rootSaga);

export default store;
