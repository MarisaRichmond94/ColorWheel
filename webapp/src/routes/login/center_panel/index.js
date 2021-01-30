import './index.scss';

import { Button, Col, FormControl, Row } from 'react-bootstrap';
import React, { useState } from 'react';
import { FaEye, FaEyeSlash } from 'react-icons/fa';

import types from '~/redux/types';

const CenterPanel = () => {
  const [isHidden, setIsHidden] = useState(true);
  const [passcode, setPasscode] = useState('');

  return (
    <Row>
      <Col id='login-panel-wrapper' xs={{ span: 6, offset: 3 }}>
        <Row className='text-center'>
          <Col xs={12}>
            <p className='title' id='secret-prompt'>
              Enter the secret code in order to continue:
						</p>
          </Col>
        </Row>
        <Row>
          <Col xs={11}>
            <FormControl
              className='remove-focus-highlight'
              id='passcode-input'
              name='passcode'
              onChange={e => setPasscode(e.target.value)}
              placeholder='super secret passcode'
              type={(isHidden) ? 'password' : 'text'}
              value={passcode}
            />
          </Col>
          <Col xs={1}>
            <Button
              className='icon-button'
              id='passcode-hide-button'
              onClick={e => setIsHidden(!isHidden)}
            >
              {(isHidden) ? <FaEye /> : <FaEyeSlash />}
            </Button>
          </Col>
        </Row>
        <Row className='text-center' style={{ marginTop: '20px' }}>
          <Col xs={12}>
            <Button
              className='text-button'
              disabled={!passcode}
              id='login-submit-button'
              onClick={e => window.dispatchAction(types.AUTHENTICATE_USER, { passcode })}
            >
              Submit
						</Button>
          </Col>
        </Row>
      </Col>
    </Row>
  );
}

export default CenterPanel;
