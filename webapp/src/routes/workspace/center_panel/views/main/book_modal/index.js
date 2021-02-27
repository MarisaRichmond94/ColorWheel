import './index.scss';

import { bool, func, object } from 'prop-types';
import React, { useState } from 'react';
import { GiOpenBook } from 'react-icons/gi';

import SmartButton from '~/components/smart_button';
import SmartModal from '~/components/smart_modal';
import types from '~/redux/types';

const BookModal = props => {
  BookModal.propTypes = {
    isModalShowing: bool.isRequired,
    selectedBook: object,
    setIsModalShowing: func.isRequired,
  };

  const [headerText, setHeaderText] = useState(props.selectedBook?.name || 'Untitled Book');

  const resetStateAndCloseModal = () => {
    props.setIsModalShowing(false);
  };

  const handleSubmit = () => {
    const action = props.selectedBook ? types.UPDATE_BOOK_DETAILS : types.CREATE_NEW_BOOK;
    const payload = props.selectedBook ? {} : {};
    window.dispatchAction(action, payload);
    props.setIsModalShowing(false);
  };

  const bodyContent = (
    <></>
  );

  return (
    <SmartModal
      bodyContent={bodyContent}
      footerContent={
        <>
          <SmartButton
            id='book-modal-cancel-button'
            onClick={() => resetStateAndCloseModal()}
            text='cancel'
          />
          <SmartButton
            isDisabled={true}
            id='book-modal-submit-button'
            onClick={() => handleSubmit()}
            text='submit'
          />
        </>
      }
      headerIcon={<GiOpenBook />}
      headerText={headerText}
      id='book-details-modal'
      isModalShowing={props.isModalShowing}
      onHideCallback={() => resetStateAndCloseModal()}
    />
  );
};

export default BookModal;
