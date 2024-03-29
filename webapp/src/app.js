import React, { useEffect } from 'react';
import { useSelector } from 'react-redux';

import AutoLogoutModal from '~/components/auto_logout_modal';
import Loading from '~/components/loading';
import Footer from '~/routes/components/footer';
import Header from '~/routes/components/header';
import LoginPage from '~/routes/login';
import SmartRouter from '~/routes/router';
import types from '~/sagas/types';

const App = () => {
  const accessToken = useSelector(state => state.user.accessToken);
  const isAuthenticatingUser = useSelector(state => state.user.isAuthenticating);

  useEffect(() => {
    if (!accessToken) {
      try {
        window.dispatchSagaAction(types.AUTHENTICATE_SESSION);
      } catch (error) {
        // eventually route to error page
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return isAuthenticatingUser
    ? <Loading />
    : accessToken
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

export default App;
