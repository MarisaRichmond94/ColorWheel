import './index.scss';

import { bool, func, string } from 'prop-types';
import React, { useState } from 'react';
import { Col, Row } from 'react-bootstrap';
import { AiOutlineLock, AiOutlineUnlock } from 'react-icons/ai';
import { FaEye, FaEyeSlash } from 'react-icons/fa';

import SmartFormInput from '~/components/smart_form_input';

const PasswordInput = props => {
  PasswordInput.propTypes = {
    isValidInput: bool.isRequired,
    password: string.isRequired,
    setPassword: func.isRequired,
    setIsValidInput: func.isRequired,
  };

  const [isHidden, setIsHidden] = useState(true);

  const validateInput = input => {
    props.setIsValidInput(
      /^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{10,}$/.test(input),
    );
  };

  return (
    <Row className='text-center input-row-wrapper'>
      <Col className='input-col-wrapper'>
        <span
          className={`inline-span password ${props.isValidInput ? 'valid-icon' : 'invalid-icon'}`}
        >
          {props.isValidInput ? <AiOutlineUnlock /> : <AiOutlineLock />}
        </span>
        <span className='inline-span password form-input-wrapper'>
          <SmartFormInput
            classNames='clear-form-input'
            formValue={props.password}
            id='password-input'
            placeholder='something super secretive... not "password"'
            setFormValue={props.setPassword}
            type={(isHidden) ? 'password' : 'text'}
            validateFormValue={validateInput}
          />
        </span>
        <span
          className='inline-span password visibility-icon'
          id='password-hide-button'
          onClick={() => setIsHidden(!isHidden)}
        >
          {(isHidden) ? <FaEye /> : <FaEyeSlash />}
        </span>
      </Col>
    </Row>
  );
};

export default PasswordInput;
