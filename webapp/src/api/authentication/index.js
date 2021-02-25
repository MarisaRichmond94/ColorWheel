import { BaseApiClass } from '~/api/base';

const AuthenticationClass = class Authentication extends BaseApiClass {
  constructor() {
    super('authentication', false);
  }

  get(email) {
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

    return super.get({ email });
  }

  post(body) {
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

    return super.post(body);
  }
};

const Singleton = new AuthenticationClass();
const AuthenticationApi = {
  post: (...params) => Singleton.post(...params),
  get: (...params) => Singleton.get(...params),
};
export default AuthenticationApi;
export { AuthenticationClass };
