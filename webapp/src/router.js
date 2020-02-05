import React from 'react';
import { Route } from 'react-router-dom';

import Home from './routes/home';
import Login from './routes/login';

function SmartRouter(props) {
	return (
		<>
			<Route exact path='/' component={Login} />
			<Route exact path='/home' component={Home} />
		</>
	)
}

export default SmartRouter;