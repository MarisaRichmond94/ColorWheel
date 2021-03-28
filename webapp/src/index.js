import 'babel-polyfill';
import './global.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Router } from 'react-router-dom';

import App from '~/app';
import history from '~/utils/history';
import store from '~/utils/store';

// set window acessible functions
window.dispatch = store.dispatch;
window.dispatchAction = (type, payload) => store.dispatch({ type, payload });
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
