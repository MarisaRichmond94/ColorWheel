import { Button, Col, FormControl, Row } from 'react-bootstrap';
import React, { useState } from 'react';

function LoginPanel(props) {
	const [passcode, setPasscode] = useState();

	const submit = () => {
		console.log(passcode);
		// TODO: call api to authenticate passcode with the backend
	}

	return (
		<Row>
			<Col id='login-panel-wrapper' xs={{ span: 6, offset: 3 }}>
				<Row className='text-center'>
					<Col xs={12}>
						<p className='title' id='secret-prompt'>
							Enter the secret code in order to continue:
						</p>
					</Col>
				</Row>
				<Row>
					<Col xs={12}>
						<FormControl
							className='remove-focus-highlight'
							id='passcode-input'
							onChange={e => setPasscode(e.target.value)}
							placeholder='super secret passcode'
							type='text'
							value={passcode}
						/>
					</Col>
				</Row>
				<Row className='text-center' style={{ marginTop: '20px' }}>
					<Col xs={12}>
						<Button className='text-button' onClick={submit}>
							Submit
						</Button>
					</Col>
				</Row>
			</Col>
		</Row>
	);
}

export default LoginPanel;