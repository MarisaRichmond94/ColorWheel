import './index.scss';

import React from 'react';
import { FaUserCog } from 'react-icons/fa';
import { IoLogOutOutline, IoSettingsOutline } from 'react-icons/io5';

import SmartDropdown from '~/components/smart_dropdown';
import types from '~/redux/types';

const CogMenu = () => {
  const options = [
    {
      displayName: 'Account',
      icon: <FaUserCog />,
      onClick: () => console.log('Eventually this will display a user settings modal'),
    },
    {
      displayName: 'Sign Out',
      icon: <IoLogOutOutline />,
      onClick: () => window.dispatchAction(types.DEAUTHENTICATE_USER),
    },
  ];

  return (
    <span className='header-icon float-right' id='header-cog-menu-button'>
      <SmartDropdown
        id='header-cog-menu-button-dropdown'
        options={options}
        title={<IoSettingsOutline />}
      />
    </span>
  );
};

export default CogMenu;
