import './index.scss';

import React from 'react';
import { Col, Row } from 'react-bootstrap';
import {
  FaCode, FaGithub, FaHackerrank, FaLinkedin, FaStackOverflow,
} from 'react-icons/fa';

const SecretFooter = () => (
  <Row id='secret-footer'>
    <Col>
      <FaGithub
        className='icon-button'
        onClick={() => window.open('https://github.com/MarisaRichmond94')}
      />
      <FaLinkedin
        className='icon-button'
        onClick={() => window.open('https://www.linkedin.com/in/marisa-richmond-4a576265/')}
      />
      <FaHackerrank
        className='icon-button'
        onClick={() => window.open('https://www.hackerrank.com/marisa_richmond1')}
      />
      <FaCode
        className='icon-button'
        onClick={() => window.open('https://leetcode.com/marisarichmond94/')}
      />
      <FaStackOverflow
        className='icon-button'
        onClick={() => window.open('https://stackoverflow.com/users/8960952/marisa-richmond')}
      />
    </Col>
  </Row>
);

export default SecretFooter;