import './index.scss';

import React from 'react';

import source from '~/assets/images/login_title.png';

const Title = () => {
  return (
    <div id='login-title'>
      <img src={source} />
    </div>
  );
}

export default Title;
