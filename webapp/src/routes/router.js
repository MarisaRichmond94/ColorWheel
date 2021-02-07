import React from 'react';
import loadable from 'react-loadable';
import { Route } from 'react-router-dom';

const LoginRoute = loadable({
  loader: () => import('./login'),
  loading: () => <></>,
});

const HomeRoute = loadable({
  loader: () => import('./home'),
  loading: () => <></>,
});

function SmartRouter() {
  return (
  <>
    <Route exact path='/' component={LoginRoute} />
    <Route exact path='/home' component={HomeRoute} />
  </>
  );
}

export default SmartRouter;
