import './index.scss';

import React from 'react';
import { useLocation } from 'react-router-dom';

import BookSelector from '~/routes/components/header/book_selector';
import CogMenu from '~/routes/components/header/cog_menu';
import Greeting from '~/routes/components/header/greeting';
import Logo from '~/routes/components/header/logo';
import NavigationMenu from '~/routes/components/header/navigation_menu';

const Header = () => {
  const location = useLocation();

  return (
    <div id='main-header'>
      <Logo />
      <NavigationMenu />
      {location.pathname.includes('workspace') && <BookSelector />}
      <CogMenu />
      <Greeting />
    </div>
  );
};

export default Header;
