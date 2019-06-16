import { applyMiddleware, createStore } from 'redux';
import autoMergeLevel2 from 'redux-persist/lib/stateReconciler/autoMergeLevel2';
import { composeWithDevTools } from 'redux-devtools-extension';
import logger from 'redux-logger';
import { PersistGate } from 'redux-persist/lib/integration/react';
import { persistReducer, persistStore } from 'redux-persist';
import { Provider } from 'react-redux';
import React from 'react';
import ReactDOM from 'react-dom';
import storage from 'redux-persist/lib/storage';

import App from './app';
import rootReducer from './redux/root-reducer';
import 'bootstrap/dist/css/bootstrap.min.css';

const persistConfig = {
  key: 'root',
  storage: storage,
  stateReconciler: autoMergeLevel2
};
const reducer = persistReducer(persistConfig, rootReducer);
const devTools = process.env.NODE_ENV === 'development'
  ? composeWithDevTools(applyMiddleware(logger))
  : undefined;
const store = createStore(
  reducer,
  undefined, //initial state
  devTools
);
const persistor = persistStore(store);

ReactDOM.render(
  <Provider store={store}>
    <PersistGate loading={null} persistor={persistor}>
      <App/>
    </PersistGate>
  </Provider>,
  document.getElementById('app')
);