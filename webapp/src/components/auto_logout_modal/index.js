import './index.scss';

import React, { useEffect, useState } from 'react';
import { FiPhoneCall } from 'react-icons/fi';
import { useSelector } from 'react-redux';

import SmartModal from '~/components/smart_modal';
import types from '~/sagas/types';
let logoutTimer;

const AutoLogoutModal = () => {
  const { isLogoutWarningModalShowing } = useSelector(state => state.user);
  const [timeRemaining, setTimeRemaining] = useState(60);

  useEffect(() => {
    if (isLogoutWarningModalShowing) {
      logoutTimer = setInterval(() => {
        const seconds = timeRemaining - 1;
        setTimeRemaining(seconds);
        if (seconds === 0) {
          setTimeRemaining(60);
          window.dispatchSagaAction(
            types.SET_IS_LOGOUT_WARNING_MODAL_SHOWING,
            { isLogoutWarningModalShowing: false },
          );
          clearInterval(logoutTimer);
        }
      }, 1000);
    } else {
      clearInterval(logoutTimer);
      setTimeRemaining(60);
    }

    return () => clearInterval(logoutTimer);
  }, [isLogoutWarningModalShowing, timeRemaining]);

  const bodyContent = (
    <>
      <p className='text-center'>You're about to get logged out for inactivity.</p>
      <p className='text-center'>Click anywhere on the page to stay signed in.</p>
      <p className='text-center'><b>{timeRemaining}</b></p>
    </>
  );

  return (
    <SmartModal
      bodyContent={bodyContent}
      headerIcon={<FiPhoneCall/>}
      headerText='Hey! Are you still there?'
      id='auto-logout-modal'
      isModalShowing={isLogoutWarningModalShowing}
      onHideCallback={() => window.dispatchSagaAction(types.AUTHENTICATE_SESSION)}
    />
  );
};

export default AutoLogoutModal;
