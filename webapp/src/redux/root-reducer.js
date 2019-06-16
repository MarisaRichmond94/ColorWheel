import { combineReducers } from 'redux';

const initialState = {
  isAuthenticated: false
};

const appState = (state = initialState, action) => {
  switch(action.type) {
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  appState,
  //add additional reducers here
});

export default rootReducer;