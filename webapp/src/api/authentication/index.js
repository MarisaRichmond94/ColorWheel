import 'isomorphic-fetch';

import { keysToCamel } from '~/utils/convertCasing';

class Authentication {
  constructor() {
    this.url = `${window?.CONFIG?.API_URL}/authentication`;
    this.useMock = window.location.search.includes('MOCK_BE');
  }

  post = async (name, email, password) => {
    if (this.useMock) {
      return true;
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
          },
          body: json.stringify({ name, email, password }),
        },
      );
    } catch (error) {
      error.message = `Failed to authorizer user: ${error.message}`;
      return;
    }
    console.log({ response })
    if (response && response.ok && response.status === 200) {
      const res = await response.json();
      return keysToCamel(res.data);
    }
  }
}

const AuthenticationApi = new Authentication();
export default AuthenticationApi;
