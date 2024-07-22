export default defineNuxtRouteMiddleware((to, from) => {
	const accessToken = useCookie('accessToken')
	console.log('Access Token: ', accessToken)
	if (!accessToken.value) {
		return navigateTo('/login')
	}
})
