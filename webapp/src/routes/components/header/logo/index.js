import './index.scss';

import React from 'react';
import { Link } from 'react-router-dom';

import icon from '~/assets/icons/colorwheel_icon.png';

const Logo = () => {
  return (
    <Link to={`/workspace${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`}>
      <span className='float-left'>
        <img alt='' id='main-header-icon' src={icon} />
        <p id='main-header-text'>ColorWheel</p>
      </span>
    </Link>
  );
};

export default Logo;
