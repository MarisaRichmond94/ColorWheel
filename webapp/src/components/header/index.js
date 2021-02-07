import './index.scss';

import React from 'react';
import { Col, Row } from 'react-bootstrap';

import icon from '~/assets/icons/colorwheel_icon.png';

const Header = () => {
  const logo = () => (
    <span>
      <img alt='' id='main-header-icon' src={icon} />
      <p id='main-header-text'>ColorWheel</p>
    </span>
  );

  return (
    <Row id='main-header'>
      <Col xs={3}>
        {logo()}
      </Col>
      <Col xs={9}>
        {/* insert project links here */}
      </Col>
    </Row>
  );
};

export default Header;
