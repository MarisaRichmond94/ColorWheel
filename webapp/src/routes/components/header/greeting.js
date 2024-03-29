import React from 'react';
import { useSelector } from 'react-redux';

const Greeting = () => {
  const { name } = useSelector(state => state.user);

  return (
    <span className='float-right' id='main-header-greeting-text'>
      Welcome Back, {name}!
    </span>
  );
};

export default Greeting;
