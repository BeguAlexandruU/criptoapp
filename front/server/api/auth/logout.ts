export default defineEventHandler(async event => {
	const accessToken = getCookie(event, 'accessToken')
	if (accessToken) {
		deleteCookie(event, 'accessToken')

		await fetch(
			'http://localhost:5001/auth/jwt/logout',
			{
				method: 'POST',
				headers: {
					accept: 'application/json',
					Authorization: `Bearer ${accessToken}`,
				},
				credentials: 'include',
			}
		)
	}
})
