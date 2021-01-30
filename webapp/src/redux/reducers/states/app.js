import types from '~/redux/types';

const initialAppState = {
  isUserAuthenticated: false,
};

const appState = (state = initialAppState, action) => {
  switch (action.type) {
    case types.SET_IS_USER_AUTHENTICATED:
      return { ...state, isUserAuthenticated: action.payload.isUserAuthenticated };
    default:
      return state;
  }
};

export default appState;
