import { createSlice } from '@reduxjs/toolkit';

import { deauthenticateUser, handleAuthResults } from '~/reducers/user/utils';

const initialState = {
  accessToken: undefined,
  authMessage: undefined,
  email: undefined,
  id: undefined,
  isAuthenticating: true,
  isLogoutWarningModalShowing: false,
  name: undefined,
};

const userState = createSlice({
  name: 'user',
  initialState,
  reducers: {
    deauthenticate: state => deauthenticateUser(state),
    update: (state, action) => handleAuthResults(state, action.payload),
    setAuthMessage: (state, action) => { state.authMessage = action.payload; },
    setIsAuthenticating: (state, action) => { state.isAuthenticating = action.payload; },
    setIsLogoutWarningModalShowing: (state, action) => {
      state.isLogoutWarningModalShowing = action.payload;
    },
  },
});

export const {
  deauthenticate,
  update,
  setAuthMessage,
  setIsAuthenticating,
  setIsLogoutWarningModalShowing,
} = userState.actions;
export default userState.reducer;
