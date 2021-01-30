import 'babel-polyfill';
import './global';

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Router } from 'react-router-dom';
import { applyMiddleware, compose, createStore } from 'redux';
import createSagaMiddleware from 'redux-saga';

import App from '~/app';
import history from '~/utils/history';
import reducer from '~/redux/reducers';
import rootSaga from '~/sagas';

// set up redux/sagas
const composeEnhancers = (process.env.NODE_ENV === 'development' && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__) || compose;
const sagaMiddleware = createSagaMiddleware();
const store = createStore(
	reducer,
	undefined,
	composeEnhancers(applyMiddleware(sagaMiddleware)),
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