import './index.scss';

import { array, bool, func, object } from 'prop-types';
import React from 'react';
import { DropdownButton, DropdownItem } from 'react-bootstrap';

const SmartDropdown = props => {
  SmartDropdown.propTypes = {
    isDisabled: bool,
    onOptionSelect: func,
    options: array,
    selectedOption: object,
    title: object.isRequired,
  };

  const populateDropdownItems = () => {
    if (!props.options || !props.options.length) {
      return (
        <DropdownItem>
          <span>
            {!props.options ? 'Loading...' : 'No options available'}
          </span>
        </DropdownItem>
      );
    } else {
      const options = (props.selectedOption)
        ? props.options.filter(option => option.displayName !== props.selectedOption.displayName)
        : props.options;
      return options.map((option, index) => {
        const content = option.icon
          ? <>{option.icon}&nbsp;&nbsp;{option.displayName}</>
          : option.displayName;
        return (
          <DropdownItem
            className='overflow-ellipsis smart-dropdown-item'
            key={`smart-dropdown-option-${index}`}
            id={`smart-dropdown-option-${index}`}
            onClick={() => option.onClick ? option.onClick() : props.onOptionSelect(option)}
          >
            {content}
          </DropdownItem>
        );
      });
    }
  };

  return (
    <DropdownButton
      className='remove-focus-highlight smart-dropdown'
      disabled={props.isDisabled || false}
      title={props.title}
    >
      {populateDropdownItems()}
    </DropdownButton>
  );
};

export default SmartDropdown;
