import loadable from 'react-loadable';
import React from 'react';
import { Route } from 'react-router-dom';

const LoginRoute = loadable({
	loader: () => import('./routes/login'),
	loading: () => <h1>Loading Login...</h1>
});

const HomeRoute = loadable({
	loader: () => import('./routes/home'),
	loading: () => <h1>Loading Home...</h1>
});

function SmartRouter(props) {
	return (
		<>
			<Route exact path='/' component={LoginRoute} />
			<Route path='/home' component={HomeRoute} />
		</>
	)
}

export default SmartRouter;
