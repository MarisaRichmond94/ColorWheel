import './index.scss';

import { object, string } from 'prop-types';
import React from 'react';
import { Col, Row } from 'react-bootstrap';
import ClipLoader from 'react-spinners/ClipLoader';

const Loading = props => {
  Loading.propTypes = {
    id: string,
    loadingIcon: object,
  };

  return (
    <Row className='loading-icon' id={props.id || ''}>
      <Col className='text-center'>
        {props.loadingIcon || <ClipLoader color='#8AE7D5' loading={true} size={150} />}
        <Col xs={12} className='text-center'>
          <h3>Loading...</h3>
        </Col>
      </Col>
    </Row>
  );
};

export default Loading;
