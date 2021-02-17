import './index.scss';

import { bool, func, object, string } from 'prop-types';
import React from 'react';
import { Modal } from 'react-bootstrap';

const SmartModal = props => {
  SmartModal.propTypes = {
    bodyContent: object,
    footerContent: object,
    headerIcon: object,
    headerText: string,
    id: string,
    isModalShowing: bool.isRequired,
    onHideCallback: func.isRequired,
  };

  return (
    <Modal
      className='smart-modal'
      id={props.id}
      onHide={() => props.onHideCallback()}
      show={props.isModalShowing}
      centered
    >
      <Modal.Header className='smart-modal-header'>
        <Modal.Title >
          {props.headerIcon}
          &nbsp;&nbsp;{props.headerText}
        </Modal.Title>
      </Modal.Header>
      <Modal.Body className='smart-modal-body'>
        {props.bodyContent}
      </Modal.Body>
      {props.footerContent &&
        <Modal.Footer className='smart-modal-footer'>
          {props.footerContent}
        </Modal.Footer>
      }
    </Modal>
  );
};

export default SmartModal;
