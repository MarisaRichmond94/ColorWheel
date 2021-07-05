import './index.scss';

import { bool, object, string } from 'prop-types';
import React from 'react';
import { Col, Row } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const SectionIcon = props => {
  SectionIcon.propTypes = {
    colorClass: string.isRequired,
    icon: object.isRequired,
    isHovered: bool.isRequired,
    text: string.isRequired,
    to: string.isRequired,
  };

  return (
    <Link to={props.to}>
      <Row className='section-icon'>
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
    </Link>
  );
};

export default SectionIcon;
