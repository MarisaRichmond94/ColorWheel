class Authentication {
	constructor() {
		this.url = 'http://localhost:8080/authentication';
	}

	authenticate = async (passcode) => {
		try {
			const res = await fetch(
				this.url,
				{
					method: 'POST',
					mode: 'cors',
					headers: {
						'Content-Type': 'application/json',
					},
					body: JSON.stringify({ passcode })
				}
			);
			return res.json();
		} catch (error) {
			console.error('Fetch failed for POST /authentication', error);
		}
	}

	reauthenticate = async () => {
		try {
			const res = await fetch(
				this.url + '/check_session',
				{
					credentials: 'include',
					method: 'POST',
					mode: 'cors',
				}
			);
			return res.json();
		} catch (error) {
			console.error('Fetch failed for POST /authentication/check_session', error);
		}
	}
}

const authenticationApi = new Authentication();
export default authenticationApi;