import './index.scss';

import React from 'react';

import CenterPanel from '~/routes/workspace/center_panel';
import LeftSidebar from '~/routes/workspace/left_sidebar';

const WorkspacePage = () => (
  <div id='workspace-page'>
    <LeftSidebar />
    <CenterPanel />
  </div>
);

export default WorkspacePage;
