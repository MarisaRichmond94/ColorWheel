import { bool, func } from 'prop-types';
import React from 'react';

import SmartButton from '~/components/smart_button';

const Prompt = props => {
  Prompt.propTypes = {
    isSignUpPage: bool.isRequired,
    setIsSignUpPage: func.isRequired,
  };

  return props.isSignUpPage
    ? (
      <div className='text-center' style={{ fontSize: '20px' }}>
        <span className='inline-span'>
          <p>Already have an account?</p>
        </span>
        <span className='inline-span'>
          <SmartButton
            className='text-button'
            id='login-prompt-login-button'
            onClick={() => props.setIsSignUpPage(false)}
            style={{ fontSize: '18px' }}
            text='Log in'
          />
        </span>
      </div>
      )
    : (
      <div className='text-center' style={{ fontSize: '20px' }}>
        <span className='inline-span'>
          <p>First time here?</p>
        </span>
        <span className='inline-span'>
          <SmartButton
            className='text-button'
            id='login-prompt-signup-button'
            onClick={() => props.setIsSignUpPage(true)}
            style={{ fontSize: '18px' }}
            text='Create an account'
          />
        </span>
      </div>
      );
};

export default Prompt;
