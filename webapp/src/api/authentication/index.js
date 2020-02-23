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
			console.error('Fetch failed for POST /authenticate', error);
		}
	}
}

const authenticationApi = new Authentication();
export default authenticationApi;