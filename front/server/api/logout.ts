export default defineEventHandler(async event => {
	const accessToken = getCookie(event, 'accessToken')
	if (accessToken) {
		deleteCookie(event, 'accessToken')
	}
})
