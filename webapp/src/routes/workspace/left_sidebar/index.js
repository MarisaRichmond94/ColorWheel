import './index.scss';

import React, { useEffect, useState } from 'react';
import { AiOutlineFileSearch } from 'react-icons/ai';
import { GiBookCover, GiBrain, GiHouse, GiLaptop, GiSpellBook } from 'react-icons/gi';
import { GoChecklist } from 'react-icons/go';

import SectionIcon from '~/routes/workspace/left_sidebar/section_icon';

const LeftSidebar = () => {
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    const leftSidebarElement = document.getElementById('workspace-left-sidebar');
    leftSidebarElement.addEventListener('mouseenter', e => setIsHovered(true));
    leftSidebarElement.addEventListener('mouseleave', e => setIsHovered(false));
  }, []);

  const buildLinkTo = view => {
    const isMock = window.location.search.includes('MOCK_BE');
    return `/workspace?view=${view}${isMock ? '&MOCK_BE' : ''}`;
  };

  return (
    <div id='workspace-left-sidebar'>
      <SectionIcon
        colorClass='red'
        icon={<GiHouse />}
        isHovered={isHovered}
        to={buildLinkTo('home')}
        text='home'
      />
      <SectionIcon
        colorClass='orange'
        icon={<GiBrain />}
        isHovered={isHovered}
        to={buildLinkTo('plan')}
        text='plan'
      />
      <SectionIcon
        colorClass='yellow'
        icon={<GiLaptop />}
        isHovered={isHovered}
        to={buildLinkTo('write')}
        text='write'
      />
      <SectionIcon
        colorClass='green'
        icon={<GoChecklist />}
        isHovered={isHovered}
        to={buildLinkTo('edit')}
        text='edit'
      />
      <SectionIcon
        colorClass='teal'
        icon={<AiOutlineFileSearch />}
        isHovered={isHovered}
        to={buildLinkTo('review')}
        text='review'
      />
      <SectionIcon
        colorClass='blue'
        icon={<GiBookCover />}
        isHovered={isHovered}
        to={buildLinkTo('revise')}
        text='revise'
      />
      <SectionIcon
        colorClass='purple'
        icon={<GiSpellBook />}
        isHovered={isHovered}
        to={buildLinkTo('publish')}
        text='publish'
      />
    </div>
  );
};

export default LeftSidebar;
