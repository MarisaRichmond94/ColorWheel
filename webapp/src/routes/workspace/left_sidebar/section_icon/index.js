import './index.scss';

import { bool, func, object, string } from 'prop-types';
import React from 'react';
import { Col, Row } from 'react-bootstrap';

const SectionIcon = props => {
  SectionIcon.propTypes = {
    colorClass: string.isRequired,
    icon: object.isRequired,
    isHovered: bool.isRequired,
    onClick: func.isRequired,
    text: string.isRequired,
  };

  return (
    <Row className='section-icon' onClick={() => props.onClick()}>
      <Col>
        <Row className='text-center'>
          <Col className={`left-sidebar-icon ${props.isHovered ? props.colorClass : 'white'}`}>
            {props.icon}
          </Col>
        </Row>
        <Row className='text-center'>
          <Col className={`left-sidebar-text ${props.isHovered ? props.colorClass : 'white'}`}>
            {props.text}
          </Col>
        </Row>
      </Col>
    </Row>
  );
};

export default SectionIcon;
