import { bool, func, string } from 'prop-types';
import { Col, Row } from 'react-bootstrap';
import React from 'react';
import { FiUserCheck, FiUserX } from 'react-icons/fi';

import SmartFormInput from '~/components/smart_form_input';

const NameInput = props => {
  NameInput.propTypes = {
    isValidInput: bool.isRequired,
    name: string.isRequired,
    setIsValidInput: func.isRequired,
    setName: func.isRequired,
  }

  const validateInput = input => {
    const names = input.split(' ');
    const validNames = names.filter(name => name.length > 1);
    props.setIsValidInput(names.length === 2 && validNames.length === 2);
  }

  return (
    <Row className='text-center input-row-wrapper'>
      <Col className='input-col-wrapper'>
        <span className={`inline-span name ${props.isValidInput ? 'valid-icon' : 'invalid-icon'}`}>
          {props.isValidInput ? <FiUserCheck /> : <FiUserX />}
        </span>
        <span className='inline-span name form-input-wrapper'>
          <SmartFormInput
            classNames='clear-form-input'
            formValue={props.name}
            id='name-input'
            placeholder='first and last name'
            setFormValue={props.setName}
            validateFormValue={validateInput}
          />
        </span>
      </Col>
    </Row>
  );
}

export default NameInput;
