export default defineEventHandler(async event => {
	const accessToken = getCookie(event, 'accessToken')
	console.log('Access Token Posts: ', accessToken)
	const response = await fetch('http://localhost:5001/post/all', {
		method: 'GET',
		headers: {
			accept: 'application/json',
			Authorization: `Bearer ${accessToken}`,
		},
		credentials: 'include',
	})
	const posts = await response.json()
	return posts
})
