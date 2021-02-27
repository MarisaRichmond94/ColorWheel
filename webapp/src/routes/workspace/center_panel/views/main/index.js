import './index.scss';

import React, { useState } from 'react';

import BookModal from '~/routes/workspace/center_panel/views/main/book_modal';

const MainPanel = () => {
  const [isBookModalShowing, setIsBookModalShowing] = useState(false);
  const [selectedBook, setSelectedBook] = useState();

  return (
    <>
      <BookModal
        isModalShowing={isBookModalShowing}
        selectedBook={selectedBook}
        setIsModalShowing={setIsBookModalShowing}
      />
      <div id='main-panel'>
        Main Panel
      </div>
    </>
  );
};

export default MainPanel;
