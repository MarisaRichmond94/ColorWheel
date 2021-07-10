import React from 'react';
import { Col, Row } from 'react-bootstrap';
import { useSelector } from 'react-redux';

import SmartButton from '~/components/smart_button';
import { useLogin } from '~/context/login';
import EmailInput from '~/routes/login/inputs/email';
import NameInput from '~/routes/login/inputs/name';
import PasswordInput from '~/routes/login/inputs/password';

const Form = () => {
  const { authMessage } = useSelector(state => state.user);
  const { getIsValidInput, isSignUpPage, onFormSubmit } = useLogin();

  return (
    <Row id='login-form'>
      <Col xs={{ span: 6, offset: 3 }}>
        <form>
          {isSignUpPage && <NameInput />}
          <EmailInput />
          <PasswordInput />
          {
            authMessage &&
            <p className='text-center' id='auth-warning-message'>{authMessage}</p>
          }
          <Row className='text-center' id='submit-button-wrapper'>
            <Col>
              <SmartButton
                isDisabled={!getIsValidInput('all')}
                id='submit-button'
                onClick={onFormSubmit}
                text={isSignUpPage ? 'Sign Up' : 'Login'}
              />
            </Col>
          </Row>
        </form>
      </Col>
    </Row>
  );
};

export default Form;
