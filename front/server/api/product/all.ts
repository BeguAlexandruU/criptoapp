export default defineEventHandler(async event => {
	const accessToken = getCookie(event, 'accessToken')
	const fetch_res = await fetch('http://localhost:5001/product/all', {
		method: 'GET',
		headers: {
			accept: 'application/json',
			Authorization: `Bearer ${accessToken}`,
		},
		credentials: 'include',
	})
	const res = await fetch_res.json()
	return res
})
