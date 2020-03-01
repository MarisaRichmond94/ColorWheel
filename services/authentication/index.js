const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const cors = require('cors');
const express = require('express');

const controller = require('./controller');

const app = express();
const ORIGIN = 'http://localhost:3000';
const PORT = 8080;

controller.connectToDB();
app.use(cors({ credentials: true, origin: ORIGIN }));
app.use(bodyParser.json());
app.use(cookieParser());

app.post('/authentication', async (req, res) => {
	await controller.authenticate(req, res);
});
app.post('/refresh', async (req, res) => {
	await controller.refresh(req, res);
});

app.listen(PORT, function () {
	console.log(`Authentication service listening on port ${PORT}...`);
});
