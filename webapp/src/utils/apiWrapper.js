import 'isomorphic-fetch';

import types from '~/redux/types';
import store from '~/store';
import { keysToCamel, keysToSnake } from '~/utils/convertCasing';

class ApiWrapper {
  constructor(route, isAuthenticatedRoute = true) {
    this.accessToken = undefined;
    this.email = undefined;
    this.isAuthenticatedRoute = isAuthenticatedRoute;
    this.url = `${window?.CONFIG?.API_URL}/${route}`;
    this.useMock = window.location.search.includes('MOCK_BE');
  }

  makeDeleteRequest = async(id, query = {}) => {
    this.updateWrapperState();
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
    this.updateWrapperState();
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
    this.updateWrapperState();
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
    this.updateWrapperState();
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

  updateWrapperState = () => {
    if (this.isAuthenticatedRoute && (!this.accessToken || !this.email)) {
      this.accessToken = store?.getState()?.userState?.accessToken;
      this.email = store?.getState()?.userState?.email;
    }
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
          email: this.email,
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
      const res = await response.json();

      if (this.isAuthenticatedRoute) {
        const { authResults, data } = keysToCamel(res.data);
        window.dispatchAction(types.HANDLE_AUTH_RESULTS, { authResults });
        return data;
      }

      return keysToCamel(res.data);
    }
  }
}

export default ApiWrapper;
