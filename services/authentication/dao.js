const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const mysql = require('mysql');
const util = require('util');

const jwtKey = 'temporary_secret_key';

const DATABASE_NAME = 'colorwheel';
const TABLES = [
	{
		name: 'authentication',
		schema: `(
			id int PRIMARY KEY auto_increment,
			hash LONGTEXT NOT NULL,
			salt LONGTEXT NOT NULL
		)`
	}
];
let CONNECTION;

function connectToDB() {
	CONNECTION = mysql.createConnection({
		host: 'localhost',
		user: 'root',
		password: 'password',
		database: DATABASE_NAME,
		insecureAuth: true,
	});
	CONNECTION.connect((error) => {
		if (error) throw error;
		console.log(`Connected to database ${DATABASE_NAME}...`);
		initializeTables();
		generateDefaults();
	});
	CONNECTION.query = util.promisify(CONNECTION.query);
}

function initializeTables() {
	TABLES.forEach(TABLE => {
		const createAuthTable = `CREATE TABLE IF NOT EXISTS ${TABLE.name}${TABLE.schema}`;
		CONNECTION.query(createAuthTable, function (error) {
			if (error) throw error;
			console.log(`Initialized ${TABLE.name} table...`);
		});
	});
}

async function generateDefaults() {
	const getCount = `SELECT COUNT(*) AS rowLength FROM ${TABLES[0].name}`;
	const count = await CONNECTION.query(getCount);
	if (count && count[0] && count[0].rowLength === 0) {
		const PASSWORD = 'hire me please';
		bcrypt.genSalt(10, function (error, SALT) {
			if (error) throw error;
			bcrypt.hash(PASSWORD, SALT, function (error, HASH) {
				if (error) throw error;
				const insertRow = `INSERT INTO ${TABLES[0].name}(hash, salt) VALUES ? `;
				const values = [[HASH, SALT]];
				CONNECTION.query(insertRow, [values], function (error) {
					if (error) throw error;
					console.log(`Populated ${TABLES[0].name} with data...`);
				});
			});
		});
	} else {
		console.log(`${TABLES[0].name} already populated with data...`);
	}
}

async function getSessionToken(passcode) {
	let sessionToken = undefined;
	const isValidPasscode = await validatePasscode(passcode);
	if (isValidPasscode) {
		sessionToken = jwt.sign({}, jwtKey, { algorithm: 'HS256', expiresIn: 300 });
	}
	return sessionToken;
}

async function validatePasscode(passcode) {
	const getPasscode = `SELECT a.hash, a.salt FROM authentication a WHERE a.id = 1`;
	let isValidPasscode = false;
	const results = await CONNECTION.query(getPasscode);
	if (results && results[0]) {
		const result = await new Promise((resolve, reject) => {
			bcrypt.compare(passcode, results[0].hash, function (error, result) {
				resolve(result)
			});
		});
		isValidPasscode = result;
	}
	return isValidPasscode;
}

function validateSession(sessionToken) {
	let newToken;
	if (sessionToken) {
		let payload;
		try {
			payload = jwt.verify(sessionToken, jwtKey);
		} catch (error) {
			console.log(`Failed during validateSession with error ${error}`);
		}
		const nowUnixSeconds = Math.round(Number(new Date()) / 1000);
		if (payload.exp - nowUnixSeconds < 30) {
			newToken = jwt.sign({}, jwtKey, { algorithm: 'HS256', expiresIn: 300 });
		}
	}
	return newToken;
}

exports.connectToDB = connectToDB;
exports.getSessionToken = getSessionToken;
exports.validateSession = validateSession;
