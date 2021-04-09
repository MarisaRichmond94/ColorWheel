import BaseApi from '~/api/base';
import { getTimeInMilliseconds } from '~/utils/datetimeHelpers';

class Authentication extends BaseApi {
  constructor() {
    super('authentication', false);
  }

  get(email) {
    if (this.useMock) {
      return {
        accessToken: 'aBcD.eFgH.iJkL',
        authResults: {
          iss: 'colorwheel',
          exp: getTimeInMilliseconds(20),
          sub: '0ea4b105-5627-49ad-a517-87c4e3925534',
          name: 'Drake Stryker',
          email,
        },
      };
    }

    return super.get({ email });
  }

  post(body) {
    if (this.useMock) {
      return {
        accessToken: 'aBcD.eFgH.iJkL',
        authResults: {
          iss: 'colorwheel',
          exp: getTimeInMilliseconds(20),
          sub: '0ea4b105-5627-49ad-a517-87c4e3925534',
          name: body.name,
          email: body.email,
        },
      };
    }

    return super.post(body);
  }
};

const AuthenticationApi = new Authentication();
export default AuthenticationApi;
