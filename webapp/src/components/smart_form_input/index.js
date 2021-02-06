import './index.scss';

import { func, string } from 'prop-types';
import { FormControl } from 'react-bootstrap';
import React from 'react';

const SmartFormInput = props => {
  SmartFormInput.propTypes = {
    classNames: string,
    formValue: string.isRequired,
    id: string.isRequired,
    placeholder: string.isRequired,
    setFormValue: func.isRequired,
    type: string,
    validateFormValue: func,
  }

  const onChange = input => {
    props.setFormValue(input);
    if (props.validateFormValue) {
      props.validateFormValue(input);
    }
  }

  return (
    <FormControl
      autoComplete="none"
      className={`remove-focus-highlight smart-form-input ${props.classNames}`}
      id={props.id}
      onChange={e => onChange(e.target.value)}
      placeholder={props.placeholder}
      spellCheck="false"
      type={props.type || 'text'}
      value={props.formValue}
    />
  );
}

export default SmartFormInput;
