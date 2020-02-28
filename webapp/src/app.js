import { bool } from 'prop-types';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import Footer from '~/components/footer';
import Header from '~/components/header';
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
			window.dispatchAction('REAUTHENTICATE_USER');
		} catch (error) {
			console.log(error); // eventually route to error page
		}
	}


	return (
		(props.isAuthenticated)
			? <>
				<Header />
				<SmartRouter />
				<Footer />
			</>
			: <Login />
	);
}

export function mapStateToProps(state) {
	return {
		isAuthenticated: state.appState.isAuthenticated,
	}
};

export default connect(mapStateToProps)(App);