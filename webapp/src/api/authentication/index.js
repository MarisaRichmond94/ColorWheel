import 'isomorphic-fetch';

import ApiWrapper from '~/utils/apiWrapper';

class Authentication extends ApiWrapper {
  constructor() {
    super('authentication', false);
  }

  get = async email => {
    if (this.useMock) {
      return {
        accessToken: 'aBcD.eFgH.iJkL',
        authResults: {
          iss: 'colorwheel',
          exp: 1200,
          sub: '0ea4b105-5627-49ad-a517-87c4e3925534',
          name: 'Drake Stryker',
          email,
        },
      };
    }

    return this.makeGetRequest({ query: { email } });
  }

  post = async body => {
    if (this.useMock) {
      return {
        accessToken: 'aBcD.eFgH.iJkL',
        authResults: {
          iss: 'colorwheel',
          exp: 1200,
          sub: '0ea4b105-5627-49ad-a517-87c4e3925534',
          name: body.name,
          email: body.email,
        },
      };
    }

    return this.makePostRequest({ body });
  }
}

const AuthenticationApi = new Authentication();
export default AuthenticationApi;
