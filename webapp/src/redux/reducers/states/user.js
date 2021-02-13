import types from '~/redux/types';

const initialUserState = {
  accessToken: undefined,
  email: undefined,
  id: undefined,
  name: undefined,
};

const userState = (state = initialUserState, action) => {
  switch (action.type) {
    case types.SET_ACCESS_TOKEN:
      return { ...state, accessToken: action.payload.accessToken };
    case types.SET_USER_EMAIL:
      return { ...state, email: action.payload.email };
    case types.SET_USER_ID:
      return { ...state, id: action.payload.id };
    case types.SET_USER_NAME:
      return { ...state, name: action.payload.name };
    default:
      return state;
  }
};

export default userState;
