export const handleAuthResults = (state, { accessToken, authResults }) => {
  const newState = { ...state, accessToken };

  authResults.id = authResults.sub;
  delete authResults.sub;

  const keys = ['email', 'name', 'id'];
  keys.forEach(key => {
    newState[key] = authResults[key];
    storeResultsInCookie({ [key]: authResults[key] });
  });

  return newState;
};

const storeResultsInCookie = payload => {
  const key = Object.keys(payload)[0];
  document.cookie = `${key}=${payload[key]}; max-age=36000;`;
};

export const deauthenticateUser = state => {
  const cookieKeys = ['email', 'name', 'id'];
  cookieKeys.forEach(key => { document.cookie = `${key}=;max-age=0`; });
  localStorage.clear();
  window.historyReplace('/');
  return {
    ...state,
    accessToken: undefined,
    email: undefined,
    id: undefined,
    name: undefined,
  };
};
