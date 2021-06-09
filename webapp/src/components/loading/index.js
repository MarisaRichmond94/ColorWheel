import './index.scss';

import { bool, object, string } from 'prop-types';
import React from 'react';
import { Col, Row } from 'react-bootstrap';
import ClipLoader from 'react-spinners/ClipLoader';

const Loading = ({ id, isLoading, loadingIcon, loadingText }) => {
  Loading.propTypes = {
    id: string,
    isLoading: bool,
    loadingIcon: object,
    loadingText: string,
  };

  return (
    <Row className='loading-icon' id={id || ''}>
      <Col className='text-center'>
        {loadingIcon || <ClipLoader color='#8AE7D5' loading={isLoading || true} size={150} />}
        <Col className='text-center'>
          <h3 className='loading-text'>{loadingText || 'Loading...'}</h3>
        </Col>
      </Col>
    </Row>
  );
};

export default Loading;
