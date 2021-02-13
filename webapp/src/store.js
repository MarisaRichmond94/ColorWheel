import { routerMiddleware } from 'react-router-redux';
import { applyMiddleware, compose, createStore } from 'redux';
import createSagaMiddleware from 'redux-saga';

import rootReducer from '~/redux/reducers';
import rootSaga from '~/sagas';
import history from '~/utils/history';

const composeEnhancers = (
  process.env.NODE_ENV === 'development' && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__
) || compose;
const sagaMiddleware = createSagaMiddleware();
const store = createStore(
  rootReducer,
  undefined,
  composeEnhancers(applyMiddleware(sagaMiddleware, routerMiddleware(history))),
);
sagaMiddleware.run(rootSaga);

export default store;
