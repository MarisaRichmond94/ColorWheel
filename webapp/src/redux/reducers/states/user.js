import { deauthenticateUser, handleAuthResults } from '~/redux/reducers/helpers/user';
import types from '~/redux/types';

const initialUserState = {
  accessToken: undefined,
  email: undefined,
  id: undefined,
  name: undefined,
};

const userState = (state = initialUserState, action) => {
  switch (action.type) {
    case types.HANDLE_AUTH_RESULTS:
      return handleAuthResults(state, action.payload.authResults);
    case types.DEAUTHENTICATE_USER:
      return deauthenticateUser(state);
    default:
      return state;
  }
};

export default userState;
