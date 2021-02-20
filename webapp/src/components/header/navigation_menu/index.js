import './index.scss';

import { object } from 'prop-types';
import React, { useEffect, useState } from 'react';
import { AiOutlineFileSearch } from 'react-icons/ai';
import { GiHamburgerMenu } from 'react-icons/gi';
import { ImBooks } from 'react-icons/im';
import { withRouter } from 'react-router';

import SmartDropdown from '~/components/smart_dropdown';

let stopNavigationMenuListener;

const NavigationMenu = props => {
  NavigationMenu.propTypes = {
    history: object.isRequired,
  };

  const [selectedOption, setSelectedOption] = useState(
    window.location.pathname.split('/').join(''),
  );

  useEffect(() => {
    stopNavigationMenuListener = props.history.listen(location => {
      const newPath = location.pathname.split('/').join('');
      if (newPath !== selectedOption) {
        setSelectedOption(newPath);
      }
    });

    return () => {
      if (stopNavigationMenuListener) stopNavigationMenuListener();
    };
  }, [props.history, selectedOption]);

  const onOptionSelect = option => {
    const isMockBE = window.location.search.includes('MOCK_BE');
    window.historyPush(`/${option.displayName.toLowerCase()}${isMockBE ? '?MOCK_BE' : ''}`);
  };

  const options = [
    { displayName: 'Explore', icon: <AiOutlineFileSearch /> },
    { displayName: 'Workspace', icon: <ImBooks /> },
  ];

  return (
    <span className='header-icon float-left' id='header-navigation-menu-button'>
      <SmartDropdown
        onOptionSelect={onOptionSelect}
        options={options}
        selectedOption={options.find(option => option.displayName.toLowerCase() === selectedOption)}
        title={<GiHamburgerMenu />}
      />
    </span>
  );
};

export default withRouter(NavigationMenu);
