import types from '~/redux/types';

const initialAppState = {
  authenticationErrorMessage: undefined,
};

const appState = (state = initialAppState, action) => {
  switch (action.type) {
    case types.SET_AUTHENTICATION_ERROR_MESSAGE:
      return { ...state, authenticationErrorMessage: action.payload.authenticationErrorMessage };
    default:
      return state;
  }
};

export default appState;
