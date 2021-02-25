import './index.scss';

import React, { useEffect, useState } from 'react';
import { AiOutlineFileSearch } from 'react-icons/ai';
import { GiBookCover, GiBrain, GiLaptop, GiSpellBook } from 'react-icons/gi';
import { GoChecklist } from 'react-icons/go';
import { IoIosPeople } from 'react-icons/io';

import SectionIcon from '~/routes/workspace/left_sidebar/section_icon';

const LeftSidebar = () => {
  const [isHovered, setIsHovered] = useState(false);

  useEffect(() => {
    const leftSidebarElement = document.getElementById('workspace-left-sidebar');
    leftSidebarElement.addEventListener('mouseenter', e => setIsHovered(true));
    leftSidebarElement.addEventListener('mouseleave', e => setIsHovered(false));
  }, []);

  const handleViewChange = view => {
    const isMock = window.location.search.includes('MOCK_BE');
    window.historyPush(`/workspace?view=${view}${isMock ? 'MOCK_BE' : ''}`);
  };

  return (
    <div id='workspace-left-sidebar'>
      <SectionIcon
        colorClass='red'
        icon={<GiBrain />}
        isHovered={isHovered}
        onClick={() => handleViewChange('plan')}
        text='plan'
      />
      <SectionIcon
        colorClass='orange'
        icon={<IoIosPeople />}
        isHovered={isHovered}
        onClick={() => handleViewChange('plot')}
        text='plot'
      />
      <SectionIcon
        colorClass='yellow'
        icon={<GiLaptop />}
        isHovered={isHovered}
        onClick={() => handleViewChange('write')}
        text='write'
      />
      <SectionIcon
        colorClass='green'
        icon={<GoChecklist />}
        isHovered={isHovered}
        onClick={() => handleViewChange('edit')}
        text='edit'
      />
      <SectionIcon
        colorClass='teal'
        icon={<AiOutlineFileSearch />}
        isHovered={isHovered}
        onClick={() => handleViewChange('review')}
        text='review'
      />
      <SectionIcon
        colorClass='blue'
        icon={<GiBookCover />}
        isHovered={isHovered}
        onClick={() => handleViewChange('revise')}
        text='revise'
      />
      <SectionIcon
        colorClass='purple'
        icon={<GiSpellBook />}
        isHovered={isHovered}
        onClick={() => handleViewChange('publish')}
        text='publish'
      />
    </div>
  );
};

export default LeftSidebar;
