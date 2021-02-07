import appTypes from './states/app';
import userTypes from './states/user';

export default {
  ...appTypes(),
  ...userTypes(),
};
