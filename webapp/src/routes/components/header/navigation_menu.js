import React, { useEffect, useState } from 'react';
import { AiOutlineFileSearch } from 'react-icons/ai';
import { GiHamburgerMenu } from 'react-icons/gi';
import { ImBooks } from 'react-icons/im';
import { useHistory, useLocation } from 'react-router-dom';

import SmartDropdown from '~/components/smart_dropdown';

let stopNavigationMenuListener;

const NavigationMenu = () => {
  const history = useHistory();
  const location = useLocation();

  const [selectedOption, setSelectedOption] = useState(
    location.pathname.split('/').join(''),
  );

  useEffect(() => {
    stopNavigationMenuListener = history.listen(loc => {
      const newPath = loc.pathname.split('/').join('');
      if (newPath !== selectedOption) {
        setSelectedOption(newPath);
      }
    });

    return () => {
      if (stopNavigationMenuListener) stopNavigationMenuListener();
    };
  }, [history, selectedOption]);

  const onOptionSelect = option => {
    const isMockBE = window.location.search.includes('MOCK_BE');
    console.log({ history, option });
    history.push(`/${option.displayName.toLowerCase()}${isMockBE ? '?MOCK_BE' : ''}`);
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

export default NavigationMenu;
