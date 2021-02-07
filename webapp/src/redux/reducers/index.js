import { combineReducers } from 'redux';

import appState from './states/app';
import userState from './states/user';

export default combineReducers({
  appState,
  userState,
});
