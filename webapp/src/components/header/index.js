import './index.scss';

import { Col, Row } from 'react-bootstrap';
import React from 'react';

import icon from '../../assets/icons/colorwheel_icon.png';

function Header(props) {
	const logo = () => {
		return (
			<span>
				<img id='main-header-icon' src={icon} />
				<p id='main-header-text'>ColorWheel</p>
			</span>
		);
	}

	return (
		<Row id='main-header'>
			<Col xs={3}>
				{logo()}
			</Col>
			<Col xs={9}>
				{/* insert project links here */}
			</Col>
		</Row>
	);
}

export default Header;
