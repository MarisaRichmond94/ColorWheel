import types from '~/redux/types';

const initialAppState = {
  accessToken: undefined,
};

const appState = (state = initialAppState, action) => {
  switch (action.type) {
    case types.SET_ACCESS_TOKEN:
      return { ...state, accessToken: action.payload.accessToken };
    default:
      return state;
  }
};

export default appState;
