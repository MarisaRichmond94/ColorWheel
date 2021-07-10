import React from 'react';
import { Col, Row } from 'react-bootstrap';
import { FiUserCheck, FiUserX } from 'react-icons/fi';

import SmartFormInput from '~/components/smart_form_input';
import { useLogin } from '~/context/login';

const NameInput = () => {
  const { getIsValidInput, name, onKeyPress, updateInput, validateInput } = useLogin();
  const isValidName = getIsValidInput('name');

  return (
    <Row className='text-center input-row-wrapper'>
      <Col className='input-col-wrapper'>
        <span className={`inline-span name ${isValidName ? 'valid-icon' : 'invalid-icon'}`}>
          {isValidName ? <FiUserCheck /> : <FiUserX />}
        </span>
        <span className='inline-span name form-input-wrapper'>
          <SmartFormInput
            classNames='clear-form-input'
            formValue={name}
            id='name-input'
            onKeyPress={onKeyPress}
            placeholder='first and last name'
            setFormValue={value => updateInput('name', value)}
            validateFormValue={value => validateInput('name', value)}
          />
        </span>
      </Col>
    </Row>
  );
};

export default NameInput;
