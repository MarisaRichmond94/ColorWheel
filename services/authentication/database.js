const bcrypt = require('bcryptjs');
const mysql = require('mysql');
const util = require('util');

const DATABASE_NAME = 'colorwheel';
const TABLE_NAME = 'authentication';
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
		initializeDB();
		generateDefaults();
	});
	CONNECTION.query = util.promisify(CONNECTION.query);
}

function initializeDB() {
	const createAuthTable = `CREATE TABLE IF NOT EXISTS ${TABLE_NAME}(
		id int PRIMARY KEY auto_increment,
		hash LONGTEXT NOT NULL,
		salt LONGTEXT NOT NULL
	)`;
	CONNECTION.query(createAuthTable, function (error) {
		if (error) throw error;
		console.log(`Initialized ${TABLE_NAME} table...`);
	})
}

function generateDefaults() {
	const PASSWORD = 'hire me please';
	bcrypt.genSalt(10, function (error, SALT) {
		if (error) throw error;
		bcrypt.hash(PASSWORD, SALT, function (error, HASH) {
			if (error) throw error;
			const insertRow = `INSERT INTO ${TABLE_NAME}(hash, salt) VALUES ? `;
			const values = [[HASH, SALT]];
			CONNECTION.query(insertRow, [values], function (error) {
				if (error) throw error;
				console.log(`Populated ${TABLE_NAME} with data...`);
			});
		});
	});
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

exports.connectToDB = connectToDB;
exports.validatePasscode = validatePasscode;
