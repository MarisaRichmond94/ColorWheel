import 'isomorphic-fetch';

import types from '~/redux/types';
import store from '~/store';
import { keysToCamel, keysToSnake } from '~/utils/convertCasing';

class ApiWrapper {
  constructor(route, isAuthenticatedRoute = true) {
    this.accessToken = store?.getState()?.userState?.accessToken;
    this.isAuthenticatedRoute = isAuthenticatedRoute;
    this.url = `${window?.CONFIG?.API_URL}/${route}`;
    this.useMock = window.location.search.includes('MOCK_BE');
  }

  makeDeleteRequest = async(id, query = {}) => {
    let response;

    try {
      response = await fetch(
        (id) ? `${this.url}/${id}` : this.buildQueryString(query),
        {
          method: 'DELETE',
          mode: 'cors',
          headers: this.getHeaders(),
        },
      );
    } catch (error) {
      this.handleError(error, 'DELETE');
    }

    return this.handleResponse(response);
  }

  makeGetRequest = async({ id, query = {} }) => {
    let response;

    try {
      response = await fetch(
        (id) ? `${this.url}/${id}` : this.buildQueryString(query),
        {
          method: 'GET',
          mode: 'cors',
          headers: this.getHeaders(),
        },
      );
    } catch (error) {
      this.handleError(error, 'GET');
    }

    return this.handleResponse(response);
  }

  makePatchRequest = async(id, body) => {
    let response;

    try {
      response = await fetch(
        `${this.url}/${id}`,
        {
          method: 'PATCH',
          mode: 'cors',
          headers: this.getHeaders(),
          body: JSON.stringify(body),
        },
      );
    } catch (error) {
      this.handleError(error, 'PATCH');
    }

    return this.handleResponse(response);
  }

  makePostRequest = async({ body }) => {
    let response;

    try {
      response = await fetch(
        this.url,
        {
          method: 'POST',
          mode: 'cors',
          headers: this.getHeaders(),
          body: JSON.stringify(body),
        },
      );
    } catch (error) {
      this.handleError(error, 'POST');
    }

    return this.handleResponse(response);
  }

  buildQueryString = query => {
    let url = `${this.url}?`;
    Object.keys(query).forEach(key => {
      url += `${keysToSnake(key)}=${encodeURIComponent(query[key])}&`;
    });
    return url.slice(0, -1);
  }

  getHeaders = () => {
    return this.isAuthenticatedRoute
      ? {
          Accept: 'application/json',
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.accessToken}`,
        }
      : {
          Accept: 'application/json',
          'Content-Type': 'application/json',
        };
  }

  handleError = (error, method) => {
    error.message = `${this.route} ${method} failed: ${error.message}`;
    // route to an error page
  }

  handleResponse = async response => {
    if (response && response.ok && response.status === 200) {
      if (this.isAuthenticatedRoute) {
        const headers = keysToCamel(response.headers);
        const authResults = {
          accessToken: headers.accessToken,
          authResults: headers.authResults,
        };
        window.dispatchAction(types.HANDLE_AUTH_RESULTS, { authResults });
      }
      const res = await response.json();
      return keysToCamel(res.data);
    }
  }
}

export default ApiWrapper;
