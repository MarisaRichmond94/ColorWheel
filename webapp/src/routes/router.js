import { string } from 'prop-types';
import React from 'react';
import loadable from 'react-loadable';
import { Redirect } from 'react-router';
import { Route } from 'react-router-dom';

const LoginRoute = loadable({
  loader: () => import('./login'),
  loading: () => <></>,
});

const WorkspaceRoute = loadable({
  loader: () => import('./workspace'),
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
  <>
    <Route exact path='/' component={LoginRoute} />
    <Route exact path='/workspace' component={WorkspaceRoute} />
    <Route render={() => <DefaultRedirect redirectPath={'/workspace'} />} />
  </>
  );
}

export default SmartRouter;
