import { bool } from 'prop-types';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import Footer from '~/components/footer';
import Header from '~/components/header';
import LoginPage from '~/routes/login';
import SmartRouter from '~/routes/router';
import types from '~/redux/types';

function App(props) {
	App.propTypes = {
		isUserAuthenticated: bool.isRequired,
	}

	useEffect(() => {
		if (!props.isUserAuthenticated) {
			try {
				window.dispatchAction(types.AUTHENTICATE_USER);
			} catch (error) {
				console.log(error); // eventually route to error page
			}
		}
	}, [props.isUserAuthenticated]);

	return props.isUserAuthenticated
		? (
			<>
				<Header />
				<div id='body-container'>
					<SmartRouter />
				</div>
				<Footer />
			</>
		)
		: <LoginPage />;
}

export function mapStateToProps(state) {
	return { isUserAuthenticated: state.appState.isUserAuthenticated }
};

export default connect(mapStateToProps)(App);
