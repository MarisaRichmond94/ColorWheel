import './index.scss';

import React, { useState } from 'react';

import Footer from './footer';
import Form from './form';
import Prompt from './prompt';
import Title from './title';

const LoginPage = () => {
  const [isSignUpPage, setIsSignUpPage] = useState(true);

  return (
    <div id='login-page'>
      <Title />
      <Form isSignUpPage={isSignUpPage} />
      <Prompt isSignUpPage={isSignUpPage} setIsSignUpPage={setIsSignUpPage} />
      <Footer />
    </div>
  );
};

export default LoginPage;
