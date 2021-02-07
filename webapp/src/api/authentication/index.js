import 'isomorphic-fetch';

import { keysToCamel } from '~/utils/convertCasing';

class Authentication {
  constructor() {
    this.url = `${window?.CONFIG?.API_URL}/authentication`;
    this.useMock = window.location.search.includes('MOCK_BE');
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
        }
      };
    }

    let response;
    try {
      response = await fetch(
        this.url,
        {
          method: 'POST',
          mode: 'cors',
          headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(body),
        },
      );
    } catch (error) {
      error.message = `Failed to authorizer user: ${error.message}`;
      return;
    }

    if (response && response.ok && response.status === 200) {
      const res = await response.json();
      return keysToCamel(res.data);
    }
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
        }
      };
    }

    let response;
    try {
      response = await fetch(
        `${this.url}?email=${email}`,
        {
          method: 'GET',
          mode: 'cors',
          headers: {
            Accept: 'application/json',
          },
        },
      );
    } catch (error) {
      error.message = `Failed to authorizer user: ${error.message}`;
      return;
    }

    if (response && response.ok && response.status === 200) {
      const res = await response.json();
      return keysToCamel(res.data);
    }
  }
}

const AuthenticationApi = new Authentication();
export default AuthenticationApi;
