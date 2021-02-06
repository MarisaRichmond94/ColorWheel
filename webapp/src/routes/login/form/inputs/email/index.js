import { bool, func, string } from 'prop-types';
import { Col, Row } from 'react-bootstrap';
import React from 'react';
import { HiOutlineMail, HiOutlineMailOpen } from 'react-icons/hi';

import SmartFormInput from '~/components/smart_form_input';

const valid_endings = ['.com', '.org', '.edu', '.gov'];

const EmailInput = props => {
  EmailInput.propTypes = {
    email: string.isRequired,
    isValidInput: bool.isRequired,
    setEmail: func.isRequired,
    setIsValidInput: func.isRequired,
  }

  const validateInput = input => {
    const hasOnlyValidCharacters = (
      /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(input)
    );
    const hasAtSymbol = input.includes('@');
    const hasValidEnding = valid_endings.includes(input.slice(-4));
    props.setIsValidInput(hasOnlyValidCharacters && hasAtSymbol && hasValidEnding);
  }

  return (
    <Row className='text-center input-row-wrapper'>
      <Col className='input-col-wrapper'>
        <span className={`inline-span email ${props.isValidInput ? 'valid-icon' : 'invalid-icon'}`}>
          {props.isValidInput ? <HiOutlineMailOpen /> : <HiOutlineMail />}
        </span>
        <span className='inline-span email form-input-wrapper'>
          <SmartFormInput
            classNames='clear-form-input'
            formValue={props.email}
            id='email-input'
            placeholder='example.email@gmail.com'
            setFormValue={props.setEmail}
            validateFormValue={validateInput}
          />
        </span>
      </Col>
    </Row>
  );
}

export default EmailInput;
