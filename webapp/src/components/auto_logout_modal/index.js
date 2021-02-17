import './index.scss';

import { bool } from 'prop-types';
import React, { useEffect, useState } from 'react';
import { FiPhoneCall } from 'react-icons/fi';
import { connect } from 'react-redux';

import SmartModal from '~/components/smart_modal';
import types from '~/redux/types';

let logoutTimer;

const AutoLogoutModal = props => {
  AutoLogoutModal.propTypes = {
    isLogoutWarningModalShowing: bool.isRequired,
  };

  const [timeRemaining, setTimeRemaining] = useState(60);

  useEffect(() => {
    if (props.isLogoutWarningModalShowing) {
      logoutTimer = setInterval(() => {
        const seconds = timeRemaining - 1;
        setTimeRemaining(seconds);
      }, 1000);
    } else {
      clearInterval(logoutTimer);
      setTimeRemaining(60);
    }

    return () => clearInterval(logoutTimer);
  }, [props.isLogoutWarningModalShowing, timeRemaining]);

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
      isModalShowing={props.isLogoutWarningModalShowing}
      onHideCallback={() => window.dispatchAction(types.AUTHENTICATE_SESSION)}
    />
  );
};

export function mapStateToProps(state) {
  return {
    isLogoutWarningModalShowing: state.userState.isLogoutWarningModalShowing,
  };
};

export default connect(mapStateToProps)(AutoLogoutModal);
