import 'isomorphic-fetch';

import { update } from '~/reducers/user';
import { keysToCamel, keysToSnake } from '~/utils/convertCasing';
import generateUUID from '~/utils/generateUUID';
import store from '~/utils/store';

const BaseApiClass = class BaseApi {
  constructor(route, isAuthenticatedRoute = true) {
    this.accessToken = undefined;
    this.email = undefined;
    this.isAuthenticatedRoute = isAuthenticatedRoute;
    this.url = `${window?.CONFIG?.API_URL}/${route}`;
    this.useMock = window.location.search.includes('MOCK_BE');
  }

  async post(body) {
    if (this.useMock) {
      body.id = generateUUID();
      return body;
    }

    let response;
    try {
      response = await fetch(
        this.url,
        {
          method: 'POST',
          mode: 'cors',
          headers: this.getHeaders(),
          body: JSON.stringify(keysToSnake(body)),
        },
      );
    } catch (error) {
      this.handleError(error, 'POST');
    }

    return this.handleResponse(response);
  }

  async get(query = {}) {
    if (this.useMock) {
      return [];
    }

    let response;
    try {
      response = await fetch(
        `${this.url}?${this.buildQueryString(query)}`,
        {
          method: 'GET',
          mode: 'cors',
          headers: this.getHeaders(),
        },
      );
    } catch (error) {
      this.handleError(error, 'GET by id');
    }

    return this.handleResponse(response);
  }

  async getById(id) {
    if (this.useMock) {
      return { id };
    }

    let response;
    try {
      response = await fetch(
        `${this.url}/${id}`,
        {
          method: 'GET',
          mode: 'cors',
          headers: this.getHeaders(),
        },
      );
    } catch (error) {
      this.handleError(error, 'GET by id');
    }

    return this.handleResponse(response);
  }

  async update(id, body) {
    if (this.useMock) {
      return { ...body, id };
    }

    let response;
    try {
      response = await fetch(
        `${this.url}/${id}`,
        {
          method: 'PATCH',
          mode: 'cors',
          headers: this.getHeaders(),
          body: JSON.stringify(keysToSnake(body)),
        },
      );
    } catch (error) {
      this.handleError(error, 'PATCH');
    }

    return this.handleResponse(response);
  }

  async delete(query = {}) {
    if (this.useMock) {
      return true;
    }

    let response;
    try {
      response = await fetch(
        `${this.url}?${this.buildQueryString(query)}`,
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

  async deleteById(id) {
    if (this.useMock) {
      return true;
    }

    let response;
    try {
      response = await fetch(
        `${this.url}/${id}`,
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

  buildQueryString = query => {
    query = keysToSnake(query);
    const queryString = Object.keys(query).reduce((accumulation, key) => {
      return accumulation + `${key}=${encodeURIComponent(query[key])}&`;
    }, '');
    return (queryString.endsWith('&')) ? queryString.slice(0, -1) : queryString;
  }

  getHeaders = () => {
    if (this.isAuthenticatedRoute && (!this.accessToken || !this.email)) {
      this.accessToken = store?.getState()?.userState?.accessToken;
      this.email = store?.getState()?.userState?.email;
    }

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
        window.dispatch(update({ authResults }));
        return data;
      }

      return keysToCamel(res.data);
    }
  }
};

const Singleton = new BaseApiClass();
const BaseApi = {
  post: (...params) => Singleton.post(...params),
  get: (...params) => Singleton.get(...params),
  getById: (...params) => Singleton.getById(...params),
  update: (...params) => Singleton.update(...params),
  delete: (...params) => Singleton.delete(...params),
  deleteById: (...params) => Singleton.deleteById(...params),
  updateWrapperState: (...params) => Singleton.updateWrapperState(...params),
  buildQueryString: (...params) => Singleton.buildQueryString(...params),
  getHeaders: (...params) => Singleton.getHeaders(...params),
  handleError: (...params) => Singleton.handleError(...params),
  handleResponse: (...params) => Singleton.handleResponse(...params),
};

export default BaseApi;
export { BaseApiClass };
