import './index.scss';

import { Col, Row } from 'react-bootstrap';
import React from 'react';
import {
	FaCode, FaGithub, FaHackerrank, FaLinkedin, FaStackOverflow
} from 'react-icons/fa';

function Footer(props) {
	return (
		<Row id='main-footer'>
			<Col xs={12}>
				<FaGithub
					className='icon-button'
					onClick={() => window.open('https://github.com/MarisaRichmond94')}
				/>
				<FaLinkedin
					className='icon-button'
					onClick={() => window.open('https://www.linkedin.com/in/marisa-richmond-4a576265/')}
				/>
				<FaHackerrank
					className='icon-button'
					onClick={() => window.open('https://www.hackerrank.com/marisa_richmond1')}
				/>
				<FaCode
					className='icon-button'
					onClick={() => window.open('https://leetcode.com/marisarichmond94/')}
				/>
				<FaStackOverflow
					className='icon-button'
					onClick={() => window.open('https://stackoverflow.com/users/8960952/marisa-richmond')}
				/>
			</Col>
		</Row>
	);
}

export default Footer;
