import React from 'react';
import { Col, Row } from 'react-bootstrap';
import { HiOutlineMail, HiOutlineMailOpen } from 'react-icons/hi';

import SmartFormInput from '~/components/smart_form_input';
import { useLogin } from '~/context/login';

const EmailInput = () => {
  const { email, getIsValidInput, onKeyPress, updateInput, validateInput } = useLogin();
  const isValidEmail = getIsValidInput('email');

  return (
    <Row className='text-center input-row-wrapper'>
      <Col className='input-col-wrapper'>
        <span className={`inline-span email ${isValidEmail ? 'valid-icon' : 'invalid-icon'}`}>
          {isValidEmail ? <HiOutlineMailOpen /> : <HiOutlineMail />}
        </span>
        <span className='inline-span email form-input-wrapper'>
          <SmartFormInput
            classNames='clear-form-input'
            formValue={email}
            id='email-input'
            onKeyPress={onKeyPress}
            placeholder='example.email@gmail.com'
            setFormValue={value => updateInput('email', value)}
            validateFormValue={value => validateInput('email', value)}
          />
        </span>
      </Col>
    </Row>
  );
};

export default EmailInput;
