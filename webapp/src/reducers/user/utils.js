import AutoLogoutScheduler from '~/libs/auto_logout_scheduler';

export const handleAuthResults = (state, { accessToken, authResults }) => {
  state.accessToken = accessToken;
  authResults.id = authResults.sub;
  delete authResults.sub;
  const minutesUntilTimeout = getMinutesUntilTimeout(authResults.exp);

  const keys = ['email', 'name', 'id'];
  keys.forEach(key => {
    state[key] = authResults[key];
    storeResultsInCookie({ [key]: authResults[key] }, minutesUntilTimeout * 60);
  });

  if (!window.autoLogoutScheduler) {
    window.autoLogoutScheduler = new AutoLogoutScheduler(minutesUntilTimeout);
    window.autoLogoutScheduler.initializeAutoLogoutInterval();
    window.autoLogoutScheduler.initializeAutoLogoutModalInterval();
  } else {
    window.autoLogoutScheduler.resetAutoLogoutInterval();
    state.isLogoutWarningModalShowing = false;
  }
};

const storeResultsInCookie = (payload, maxAgeInSeconds) => {
  const key = Object.keys(payload)[0];
  document.cookie = `${key}=${payload[key]}; max-age=${maxAgeInSeconds};`;
};

export const getMinutesUntilTimeout = exp => {
  const now = new Date().getTime();
  const expirationInMilliseconds = exp * 1000;
  const differenceInMilliseconds = (expirationInMilliseconds - now);
  return Math.round(((differenceInMilliseconds % 86400000) % 3600000) / 60000);
};

export const deauthenticateUser = state => {
  state.accessToken = undefined;
  state.authMessage = undefined;
  state.email = undefined;
  state.id = undefined;
  state.isAuthenticating = false;
  state.isLogoutWarningModalShowing = false;
  state.name = undefined;
};
