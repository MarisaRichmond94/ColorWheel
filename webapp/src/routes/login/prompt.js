import React from 'react';

import SmartButton from '~/components/smart_button';
import { useLogin } from '~/context/login';

const Prompt = () => {
  const { isSignUpPage, setIsSignUpPage } = useLogin();

  return isSignUpPage
    ? (
      <div className='login-prompt text-center'>
        <span className='inline-span'>
          <p>Already have an account?</p>
        </span>
        <span className='inline-span'>
          <SmartButton
            className='text-button'
            id='login-prompt-login-button'
            onClick={() => setIsSignUpPage(false)}
            text='Log in'
          />
        </span>
      </div>
      )
    : (
      <div className='login-prompt text-center'>
        <span className='inline-span'>
          <p>First time here?</p>
        </span>
        <span className='inline-span'>
          <SmartButton
            className='text-button'
            id='login-prompt-signup-button'
            onClick={() => setIsSignUpPage(true)}
            text='Create an account'
          />
        </span>
      </div>
      );
};

export default Prompt;
