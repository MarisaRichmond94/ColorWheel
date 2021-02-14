import types from '~/redux/types';

const initialAppState = {
  authenticationErrorMessage: undefined,
  isAuthenticatingUser: true,
};

const appState = (state = initialAppState, action) => {
  switch (action.type) {
    case types.SET_AUTHENTICATION_ERROR_MESSAGE:
      return { ...state, authenticationErrorMessage: action.payload.authenticationErrorMessage };
    case types.SET_IS_AUTHENTICATING_USER:
      return { ...state, isAuthenticatingUser: action.payload.isAuthenticatingUser };
    default:
      return state;
  }
};

export default appState;
