import '~/app.scss';

import { bool, string } from 'prop-types';
import React, { useEffect } from 'react';
import { Col, Row } from 'react-bootstrap';
import { connect } from 'react-redux';
import ClipLoader from 'react-spinners/ClipLoader';

import AutoLogoutModal from '~/components/auto_logout_modal';
import Footer from '~/components/footer';
import Header from '~/components/header';
import types from '~/redux/types';
import LoginPage from '~/routes/login';
import SmartRouter from '~/routes/router';

function App(props) {
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

  const buildLoadingPane = () => {
    return (
      <Row id='login-loading-pane'>
        <Col className='text-center'>
          <ClipLoader color='#8AE7D5' loading={true} size={150} />
          <Col xs={12} className='text-center' style={{ paddingTop: '20px' }}>
            <h3 style={{ color: 'white' }}>Loading...</h3>
          </Col>
        </Col>
      </Row>
    );
  };

  return props.isAuthenticatingUser
    ? buildLoadingPane()
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
}

export function mapStateToProps(state) {
  return {
    accessToken: state.userState.accessToken,
    isAuthenticatingUser: state.userState.isAuthenticatingUser,
  };
};

export default connect(mapStateToProps)(App);
