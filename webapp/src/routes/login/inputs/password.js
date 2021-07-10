import './password.scss';

import React, { useState } from 'react';
import { Col, Row } from 'react-bootstrap';
import { AiOutlineLock, AiOutlineUnlock } from 'react-icons/ai';
import { FaEye, FaEyeSlash } from 'react-icons/fa';

import SmartFormInput from '~/components/smart_form_input';
import { useLogin } from '~/context/login';

const PasswordInput = () => {
  const { getIsValidInput, password, onKeyPress, updateInput, validateInput } = useLogin();
  const [isHidden, setIsHidden] = useState(true);
  const isValidPassword = getIsValidInput('password');

  return (
    <Row className='text-center input-row-wrapper'>
      <Col className='input-col-wrapper'>
        <span
          className={`inline-span password ${isValidPassword ? 'valid-icon' : 'invalid-icon'}`}
        >
          {isValidPassword ? <AiOutlineUnlock /> : <AiOutlineLock />}
        </span>
        <span className='inline-span password form-input-wrapper'>
          <SmartFormInput
            classNames='clear-form-input'
            formValue={password}
            id='password-input'
            onKeyPress={onKeyPress}
            placeholder='something super secretive... not "password"'
            setFormValue={value => updateInput('password', value)}
            type={(isHidden) ? 'password' : 'text'}
            validateFormValue={value => validateInput('password', value)}
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
