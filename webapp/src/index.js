import './global';

import React from 'react';
import ReactDOM from 'react-dom';
import { Col, Row } from 'react-bootstrap';

function App(props) {
	return (
		<Row>
			<Col xs={12}>
			</Col>
		</Row>
	);
}

ReactDOM.render(<App />, document.getElementById('app'));