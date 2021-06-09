import BaseApi from '~/api/base';
import { update } from '~/reducers/user';

const authConfigMiddleware = store => next => action => {
  switch (action.type) {
    case update.type:
      BaseApi.setAccessToken(action.payload.accessToken);
      BaseApi.setEmail(action.payload.authResults.email);
      break;
    default:
      break;
  }

  return next(action);
};

export default authConfigMiddleware;
