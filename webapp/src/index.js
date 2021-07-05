import 'babel-polyfill';
import '~/app.scss';

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';

import App from '~/app';
import history from '~/utils/history';
import store from '~/utils/store';

// window acessible functions
window.dispatchReduxAction = store.dispatch;
window.dispatchSagaAction = (type, payload) => store.dispatch({ type, payload });
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
