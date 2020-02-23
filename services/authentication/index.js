const bodyParser = require('body-parser');
const cors = require('cors');
const express = require('express');

const database = require('./database');

const app = express();
const PORT = 8080;

database.connectToDB();

app.use(cors());
app.use(bodyParser.json());

app.post('/authentication', async (req, res) => {
	const isValidPasscode = await database.validatePasscode(req.body.passcode);
	res.status(200).send(isValidPasscode);
});

app.listen(PORT, function () {
	console.log(`Authentication service listening on port ${PORT}...`);
});
