import './index.scss';

import { bool } from 'prop-types';
import { Col, Row } from 'react-bootstrap';
import React, { useState } from 'react';

import SmartButton from '~/components/smart_button';
import types from '~/redux/types';

import EmailInput from './inputs/email';
import NameInput from './inputs/name';
import PasswordInput from './inputs/password';

const Form = props => {
  Form.propTypes = {
    isSignUpPage: bool.isRequired,
  }

  const [name, setName] = useState('');
  const [isValidName, setIsValidName] = useState(false);
  const [email, setEmail] = useState('');
  const [isValidEmail, setIsValidEmail] = useState(false);
  const [password, setPassword] = useState('');
  const [isValidPassword, setIsValidPassword] = useState(false);

  const signUpButton = (
    <SmartButton
      isDisabled={!isValidName || !isValidEmail || !isValidPassword}
      id='signup-submit-button'
      onClick={() => window.dispatchAction(types.AUTHENTICATE_USER, { name, email, password })}
      text='Sign Up'
    />
  );

  const loginButton = (
    <SmartButton
      isDisabled={!isValidEmail || !isValidPassword}
      id='login-submit-button'
      onClick={() => window.dispatchAction(types.AUTHENTICATE_USER, { email, password })}
      text='Login'
    />
  );

  return (
    <Row id='login-form'>
      <Col xs={{ span: 6, offset: 3 }}>
        {
          props.isSignUpPage && (
            <NameInput
              isValidInput={isValidName}
              name={name}
              setIsValidInput={setIsValidName}
              setName={setName}
            />
          )
        }
        <EmailInput
          isValidInput={isValidEmail}
          email={email}
          setIsValidInput={setIsValidEmail}
          setEmail={setEmail}
        />
        <PasswordInput
          isValidInput={isValidPassword}
          password={password}
          setIsValidInput={setIsValidPassword}
          setPassword={setPassword}
        />
        <Row className='text-center' style={{ marginTop: '20px' }}>
          <Col>
            {props.isSignUpPage ? signUpButton : loginButton}
          </Col>
        </Row>
      </Col>
    </Row>
  );
}

export default Form;