class Authentication {
	constructor() {
		this.url = 'http://localhost:8080/authentication';
	}

	authenticate = async (passcode) => {
		try {
			return await fetch(
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
		} catch (error) {
			console.error('Fetch failed for POST /authenticate', error);
		}
	}
}

const authenticationApi = new Authentication();
export default authenticationApi;