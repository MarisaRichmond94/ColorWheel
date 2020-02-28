import './index.scss';

import { Col, Row } from 'react-bootstrap';
import React from 'react';

function Header(props) {
	const logo = () => {
		return (
			<p>ColorWheel</p>
		);
	}

	return (
		<Row id='main-header'>
			<Col xs={2}>
				{logo()}
			</Col>
			<Col xs={10}>
			</Col>
		</Row>
	);
}

export default Header;
