const dao = require('./dao');

const jwtDuration = 300;

function connectToDB() {
	dao.connectToDB();
}

async function authenticate(req, res) {
	const passcode = (req.body) ? req.body.passcode : undefined;
	const sessionToken = await dao.getSessionToken(passcode);
	res.status((sessionToken) ? 200 : 401);
	if (sessionToken) {
		res.cookie(
			'token',
			sessionToken,
			{ maxAge: jwtDuration * 1000, httpOnly: true, sameSite: true }
		);
	}
	res.send(!!(sessionToken));
}

function refresh(req, res) {
	const sessionToken = (req.cookies) ? req.cookies.token : undefined;
	const newToken = dao.validateSession(sessionToken);
	res.status((sessionToken || newToken) ? 200 : 401);
	if (newToken) {
		res.cookie(
			'token',
			newToken,
			{ maxAge: jwtDuration * 1000, httpOnly: true, sameSite: true }
		);
	}
	res.send((!!(newToken) || !!(sessionToken)));
}

exports.authenticate = authenticate;
exports.refresh = refresh;
exports.connectToDB = connectToDB;
