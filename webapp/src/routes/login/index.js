import './index.scss';

import React from 'react';

import { LoginProvider } from '~/context/login';
import Footer from '~/routes/login/footer';
import Form from '~/routes/login/form';
import Prompt from '~/routes/login/prompt';
import Title from '~/routes/login/title';

const LoginPage = () => {
  return (
    <LoginProvider>
      <div id='login-page'>
        <Title />
        <Form />
        <Prompt />
        <Footer />
      </div>
    </LoginProvider>
  );
};

export default LoginPage;
