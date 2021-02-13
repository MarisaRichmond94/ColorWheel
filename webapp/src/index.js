import 'babel-polyfill';
import './global.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Router } from 'react-router-dom';

import App from '~/app';
import store from '~/store';
import history from '~/utils/history';

// set window acessible functions
const action = (type, payload) => store.dispatch({ type, payload });
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
  document.getElementById('app'),
);
