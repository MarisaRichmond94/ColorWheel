const bodyParser = require('body-parser');
const cors = require('cors');
const express = require('express');

const app = express();
const PORT = 8080;

app.use(cors());
app.use(bodyParser.json());

app.post('/authentication', (req, res) => {
	// TODO - handle passcode
});

app.listen(PORT, function () {
	console.log(`Authentication service listening on port ${PORT}...`);
});
