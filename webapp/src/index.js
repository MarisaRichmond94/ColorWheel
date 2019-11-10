import './global';

import React from 'react';
import ReactDOM from 'react-dom';

function App(props) {
	return (
		<h2 className={styles.red}>Color Wheel</h2>
	);
}

ReactDOM.render(<App />, document.getElementById('app'));