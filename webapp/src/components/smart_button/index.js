import './index.scss';

import { bool, func, object, string } from 'prop-types';
import { Button } from 'react-bootstrap';
import React from 'react';

const SmartButton = props => {
  SmartButton.propTypes = {
    className: string,
    icon: string,
    id: string.isRequired,
    isDisabled: bool,
    onClick: func.isRequired,
    style: object,
    text: string,
    textBlock: object,
  }

  return (
    <Button
      className={`smart-button${` ${props.className}` || ''}`}
      disabled={props.isDisabled || false}
      id={props.id}
      onClick={props.onClick}
      style={props.style || {}}
    >
      {props.icon}
      {props.text || props.textBlock || ''}
    </Button>
  );
}

export default SmartButton;
