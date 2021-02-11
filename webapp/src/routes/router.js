import React from 'react';
import loadable from 'react-loadable';
import { Route } from 'react-router-dom';

const LoginRoute = loadable({
  loader: () => import('./login'),
  loading: () => <></>,
});

const WorkspaceRoute = loadable({
  loader: () => import('./workspace'),
  loading: () => <></>,
});

function SmartRouter() {
  return (
  <>
    <Route exact path='/' component={LoginRoute} />
    <Route exact path='/workspace' component={WorkspaceRoute} />
  </>
  );
}

export default SmartRouter;
