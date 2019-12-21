import { combineReducers } from 'redux';

import appState from './states/app';

const rootReducer = combineReducers({
	appState
});

export default rootReducer;