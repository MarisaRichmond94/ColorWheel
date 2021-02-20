import './index.scss';

import React from 'react';

import icon from '~/assets/icons/colorwheel_icon.png';

const Logo = () => {
  const routeBackToHome = () => {
    window.historyPush(`/workspace${window.location.search.includes('MOCK_BE') ? '?MOCK_BE' : ''}`);
  };

  return (
    <span className='float-left'>
      <span onClick={routeBackToHome}>
        <img alt='' id='main-header-icon' src={icon} />
        <p id='main-header-text'>ColorWheel</p>
      </span>
    </span>
  );
};

export default Logo;
