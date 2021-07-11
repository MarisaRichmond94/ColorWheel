import './index.scss';

import React from 'react';
import { Col, Row } from 'react-bootstrap';

import SmartButton from '~/components/smart_button';

const ExplorePage = () => {
  return (
    <div id='explore-page'>
      <Row className='text-center'>
        <Col>
          <Row>
            <Col xs={7}>
              <h1 id='explore-header'>Your Adventure Is About To Begin</h1>
            </Col>
          </Row>
          <Row>
            <Col xs={7}>
              <h5 id='explore-text'>
                Coming soon--a unique experience that will allow you to not only share your work
                with the world but experience all kinds of new adventures through exploring new
                worlds created by your friends and the friends you just haven't met yet.
              </h5>
            </Col>
          </Row>
          <Row>
            <Col xs={7} className='text-center' id='explore-button-wrapper'>
              <SmartButton
                className='outline-button'
                id='explore-notify-button'
                onClick={() => console.log('Sucker! This is just a placebo button, you fool!')}
                text='Notify Me'
              />
            </Col>
          </Row>
        </Col>
      </Row>
    </div>
  );
};

export default ExplorePage;
