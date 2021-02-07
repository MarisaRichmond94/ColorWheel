import { string } from 'prop-types';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import Footer from '~/components/footer';
import Header from '~/components/header';
import LoginPage from '~/routes/login';
import SmartRouter from '~/routes/router';
import types from '~/redux/types';

function App(props) {
	App.propTypes = {
		accessToken: string,
	}

	useEffect(() => {
		if (!props.accessToken) {
			try {
				window.dispatchAction(types.AUTHENTICATE_SESSION);
			} catch (error) {
				// eventually route to error page
			}
		}
	}, [props.accessToken]);

	return props.accessToken
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
	return { accessToken: state.userState.accessToken }
};

export default connect(mapStateToProps)(App);
