import { bool } from 'prop-types';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import Login from '~/routes/login';
import SmartRouter from '~/router';

function App(props) {
	App.propTypes = {
		isAuthenticated: bool.isRequired,
	}

	useEffect(() => {
		authenticateUser();
	}, []);

	const authenticateUser = () => {
		try {
			const path = window.location.pathname;
			if (!props.isAuthenticated && path !== '/login') {
				window.location = '/login';
			}
		} catch (error) {
			console.log(error); // eventually route to error page
		}
	}


	return (
		(props.isAuthenticated) ? <SmartRouter /> : <Login />
	);
}

export function mapStateToProps(state) {
	return {
		isAuthenticated: state.appState.isAuthenticated,
	}
};

export default connect(mapStateToProps)(App);