import AutoLogoutScheduler from '~/libs/auto_logout_scheduler';

export const handleAuthResults = (state, { accessToken, authResults }) => {
  const newState = { ...state, accessToken };
  authResults.id = authResults.sub;
  delete authResults.sub;

  const keys = ['email', 'name', 'id'];
  keys.forEach(key => {
    newState[key] = authResults[key];
    storeResultsInCookie({ [key]: authResults[key] });
  });

  if (!newState.autoLogoutScheduler) {
    const minutesUntilTimeout = getMinutesUntilTimeout(authResults.exp);
    newState.autoLogoutScheduler = new AutoLogoutScheduler(minutesUntilTimeout);
    newState.autoLogoutScheduler.initializeAutoLogoutInterval();
    newState.autoLogoutScheduler.initializeAutoLogoutModalInterval();
  } else {
    newState.autoLogoutScheduler.resetAutoLogoutInterval();
    newState.isLogoutWarningModalShowing = false;
  }

  return newState;
};

const storeResultsInCookie = payload => {
  const key = Object.keys(payload)[0];
  document.cookie = `${key}=${payload[key]}; max-age=36000;`;
};

export const getMinutesUntilTimeout = exp => {
  const now = new Date().getTime();
  const expirationInMilliseconds = exp * 1000;
  const differenceInMilliseconds = (expirationInMilliseconds - now);
  return Math.round(((differenceInMilliseconds % 86400000) % 3600000) / 60000);
};

export const deauthenticateUser = state => {
  const cookieKeys = ['email', 'name', 'id'];
  cookieKeys.forEach(key => { document.cookie = `${key}=;max-age=0`; });
  localStorage.clear();
  window.historyReplace('/');
  state.autoLogoutScheduler = null;

  return {
    ...state,
    accessToken: undefined,
    autoLogoutScheduler: undefined,
    email: undefined,
    id: undefined,
    name: undefined,
  };
};
