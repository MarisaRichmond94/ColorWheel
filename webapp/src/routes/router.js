import loadable from 'react-loadable';
import React from 'react';
import { Route } from 'react-router-dom';

const LoginRoute = loadable({
	loader: () => import('~/routes/login'),
	loading: () => <></>
});

const HomeRoute = loadable({
	loader: () => import('~/routes/home'),
	loading: () => <></>
});

function SmartRouter() {
	return (
  <>
    <Route exact path='/login' component={LoginRoute} />
    <Route exact path='/' component={HomeRoute} />
  </>
	)
}

export default SmartRouter;
