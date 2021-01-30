import './index.scss';

import { Col, Row } from 'react-bootstrap';
import React from 'react';

const Footer = () => {
  return (
    <Row id='main-footer'>
      <Col>
        <p style={{ color: 'white', margin: '0', padding: '5px' }}>
          Created By Marisa Richmond
        </p>
      </Col>
    </Row>
  );
}

export default Footer;
