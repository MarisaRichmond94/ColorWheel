class Authentication {
	constructor() {
		this.url = 'http://localhost:8080/';
	}

	authenticate = async (passcode) => {
		try {
			const res = await fetch(
				this.url + 'authentication',
				{
					credentials: 'include',
					method: 'POST',
					mode: 'cors',
					headers: {
						'Access-Control-Allow-Origin': '*',
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
				this.url + 'refresh',
				{
					credentials: 'include',
					method: 'POST',
					mode: 'cors',
					headers: {
						'Access-Control-Allow-Origin': '*',
					},
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