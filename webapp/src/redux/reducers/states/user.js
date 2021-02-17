import { deauthenticateUser, handleAuthResults } from '~/redux/reducers/helpers/user';
import types from '~/redux/types';

const initialUserState = {
  accessToken: undefined,
  authenticationErrorMessage: undefined,
  autoLogoutScheduler: undefined,
  email: undefined,
  id: undefined,
  isAuthenticatingUser: true,
  isLogoutWarningModalShowing: false,
  name: undefined,
};

const userState = (state = initialUserState, action) => {
  switch (action.type) {
    case types.HANDLE_AUTH_RESULTS:
      return handleAuthResults(state, action.payload.authResults);
    case types.DEAUTHENTICATE_USER:
      return deauthenticateUser(state);
    case types.SET_AUTHENTICATION_ERROR_MESSAGE:
      return { ...state, authenticationErrorMessage: action.payload.authenticationErrorMessage };
    case types.SET_AUTO_LOGOUT_SCHEDULER:
      return { ...state, autoLogoutScheduler: action.payload.autoLogoutScheduler };
    case types.SET_IS_AUTHENTICATING_USER:
      return { ...state, isAuthenticatingUser: action.payload.isAuthenticatingUser };
    case types.SET_IS_LOGOUT_WARNING_MODAL_SHOWING:
      return { ...state, isLogoutWarningModalShowing: action.payload.isLogoutWarningModalShowing };
    default:
      return state;
  }
};

export default userState;
