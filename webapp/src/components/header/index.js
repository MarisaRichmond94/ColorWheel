import './index.scss';

import React from 'react';

import BookSelector from '~/components/header/book_selector';
import CogMenu from '~/components/header/cog_menu';
import Greeting from '~/components/header/greeting';
import Logo from '~/components/header/logo';
import NavigationMenu from '~/components/header/navigation_menu';

const Header = () => {
  return (
    <div id='main-header'>
      <Logo />
      <NavigationMenu />
      {window.location.pathname.includes('workspace') && <BookSelector />}
      <CogMenu />
      <Greeting />
    </div>
  );
};

export default Header;
