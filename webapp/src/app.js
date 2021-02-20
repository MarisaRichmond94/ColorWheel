import '~/app.scss';

import { bool, string } from 'prop-types';
import React, { useEffect } from 'react';
import { connect } from 'react-redux';

import AutoLogoutModal from '~/components/auto_logout_modal';
import Footer from '~/components/footer';
import Header from '~/components/header';
import Loading from '~/components/loading';
import types from '~/redux/types';
import LoginPage from '~/routes/login';
import SmartRouter from '~/routes/router';

const App = props => {
  App.propTypes = {
    accessToken: string,
    isAuthenticatingUser: bool.isRequired,
  };

  useEffect(() => {
    if (!props.accessToken) {
      try {
        window.dispatchAction(types.AUTHENTICATE_SESSION);
      } catch (error) {
        // eventually route to error page
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return props.isAuthenticatingUser
    ? <Loading />
    : props.accessToken
      ? (
          <>
            <AutoLogoutModal />
            <Header />
            <div id='body-container'>
              <SmartRouter />
            </div>
            <Footer />
          </>
        )
      : <LoginPage />;
};

export function mapStateToProps(state) {
  return {
    accessToken: state.userState.accessToken,
    isAuthenticatingUser: state.userState.isAuthenticatingUser,
  };
};

export default connect(mapStateToProps)(App);
