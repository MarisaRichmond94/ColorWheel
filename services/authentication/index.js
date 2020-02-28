const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const cors = require('cors');
const express = require('express');

const controller = require('./controller');

const app = express();
const PORT = 8080;
const jwtDuration = 300;

controller.connectToDB();

app.use(cors());
app.use(bodyParser.json());
app.use(cookieParser());

app.post('/authentication/check_session', (req, res) => {
	let isAuthenticated = false;
	const sessionToken = (req.cookies) ? req.cookies.token : undefined;
	if (sessionToken) {
		isAuthenticated = controller.checkSession(sessionToken);
	}
	res.status((isAuthenticated) ? 200 : 401).end();
});

app.post('/authentication', async (req, res) => {
	const sessionToken = await controller.getSessionToken(req.body.passcode);
	res.status((sessionToken) ? 200 : 401);
	if (sessionToken) res.cookie('token', sessionToken, { maxAge: jwtDuration * 1000 });
	res.send(!!(sessionToken));
});

app.listen(PORT, function () {
	console.log(`Authentication service listening on port ${PORT}...`);
});
