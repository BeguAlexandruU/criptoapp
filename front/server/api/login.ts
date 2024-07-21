export default defineEventHandler(async event => {
	try {
		const { email, password } = await readBody(event)
		const response: Response = await fetch(
			'http://localhost:5001/auth/jwt/login',
			{
				method: 'POST',
				headers: {
					accept: 'application/json',
					'Content-Type': 'application/x-www-form-urlencoded',
				},
				body: `grant_type=&username=${encodeURIComponent(
					email
				)}&password=${encodeURIComponent(
					password
				)}&scope=&client_id=&client_secret=`, // Adjust the body content as needed for your request
				credentials: 'include', // This will include cookies in the request and response
			}
		)

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		const d = new Date()
		d.setTime(d.getTime() + 1 * 60 * 60 * 1000)
		const data: AccessTokenData = await response.json()
		const access_token: string = data.access_token

		setCookie(event, 'accessToken', access_token, {
			sameSite: 'none',
			secure: true,
			path: '/',
			expires: d,
		})

		return 'Success'
	} catch (error) {
		console.error('Error fetching posts', error)
		// Handle the error as needed in your application
		return { error: 'Failed to fetch posts' }
	}
})
