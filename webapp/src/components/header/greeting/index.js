import './index.scss';

import { string } from 'prop-types';
import React from 'react';
import { connect } from 'react-redux';

const Greeting = props => {
  Greeting.propTypes = {
    name: string.isRequired,
  };

  return (
    <span className='float-right' id='main-header-greeting-text'>
      Welcome Back, {props.name}!
    </span>
  );
};

export function mapStateToProps(state) {
  return {
    name: state.userState.name,
  };
};

export default connect(mapStateToProps)(Greeting);
