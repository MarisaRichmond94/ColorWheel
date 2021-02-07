import types from '~/redux/types';

const initialAppState = {
  accessToken: undefined,
  authenticationErrorMessage: undefined,
};

const appState = (state = initialAppState, action) => {
  switch (action.type) {
    case types.SET_ACCESS_TOKEN:
      return { ...state, accessToken: action.payload.accessToken };
    case types.SET_AUTHENTICATION_ERROR_MESSAGE:
      return { ...state, authenticationErrorMessage: action.payload.authenticationErrorMessage };
    default:
      return state;
  }
};

export default appState;
