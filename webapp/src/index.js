import 'babel-polyfill';
import './global.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Router } from 'react-router-dom';
import { routerMiddleware } from 'react-router-redux';
import { applyMiddleware, compose, createStore } from 'redux';
import createSagaMiddleware from 'redux-saga';

import App from '~/app';
import history from '~/utils/history';
import rootReducer from '~/redux/reducers';
import rootSaga from '~/sagas';

// set up redux/sagas/sockets (eventually)
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
const action = (type, payload) => store.dispatch({ type, payload });

// set window acessible functions
window.dispatchAction = action;
window.historyPush = history.push;
window.historyReplace = history.replace;

// root component
ReactDOM.render(
  <Provider store={store}>
    <Router history={history}>
      <App />
    </Router>
  </Provider>,
	document.getElementById('app')
);