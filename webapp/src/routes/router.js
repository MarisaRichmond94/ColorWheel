import { string } from 'prop-types';
import React from 'react';
import loadable from 'react-loadable';
import { Redirect, Route, Switch } from 'react-router-dom';

const LoginRoute = loadable({
  loader: () => import('./login'),
  loading: () => <></>,
});

const WorkspaceRoute = loadable({
  loader: () => import('./workspace'),
  loading: () => <></>,
});

const ExploreRoute = loadable({
  loader: () => import('./explore'),
  loading: () => <></>,
});

const DefaultRedirect = props => {
  DefaultRedirect.propTypes = {
    redirectPath: string,
  };
  const isMock = window.location.search.includes('MOCK_BE');
  const redirectPath = `${props.redirectPath}${isMock ? '?MOCK_BE' : ''}`;
  return <Redirect to={redirectPath} />;
};

function SmartRouter() {
  return (
    <Switch>
      <Route path='/explore' component={ExploreRoute} />
      <Route path='/workspace' component={WorkspaceRoute} />
      <Route path='/' component={LoginRoute} />
      <Route render={() => <DefaultRedirect redirectPath={'/workspace'} />} />
    </Switch>
  );
}

export default SmartRouter;
