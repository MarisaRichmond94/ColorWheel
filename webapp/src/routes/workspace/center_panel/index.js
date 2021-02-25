import './index.scss';

import { object } from 'prop-types';
import React, { useEffect, useState } from 'react';
import { withRouter } from 'react-router';

import EditPanel from '~/routes/workspace/center_panel/views/edit';
import MainPanel from '~/routes/workspace/center_panel/views/main';
import PlanPanel from '~/routes/workspace/center_panel/views/plan';
import PlotPanel from '~/routes/workspace/center_panel/views/plot';
import PublishPanel from '~/routes/workspace/center_panel/views/publish';
import ReviewPanel from '~/routes/workspace/center_panel/views/review';
import RevisePanel from '~/routes/workspace/center_panel/views/revise';
import WritePanel from '~/routes/workspace/center_panel/views/write';

let stopCenterPanelListener;

const CenterPanel = props => {
  CenterPanel.propTypes = {
    history: object.isRequired,
  };

  const [view, setView] = useState(<MainPanel />);

  useEffect(() => {
    stopCenterPanelListener = props.history.listen(location => {
      const search = new URLSearchParams(location.search);
      switch (search.get('view')) {
        case 'plan':
          setView(<PlanPanel />);
          return;
        case 'plot':
          setView(<PlotPanel />);
          return;
        case 'write':
          setView(<WritePanel />);
          return;
        case 'edit':
          setView(<EditPanel />);
          return;
        case 'review':
          setView(<ReviewPanel />);
          return;
        case 'revise':
          setView(<RevisePanel />);
          return;
        case 'publish':
          setView(<PublishPanel />);
          return;
        default:
          setView(<MainPanel />);
      }
    });

    return () => {
      if (stopCenterPanelListener) stopCenterPanelListener();
    };
  }, [props.history]);

  return (
    <div id='center-panel-wrapper'>
      {view}
    </div>
  );
};

export default withRouter(CenterPanel);
