export default defineNuxtRouteMiddleware((to, from) => {
	const nuxtApp = useNuxtApp()
	const accessToken = useCookie('accessToken')
	if (!accessToken.value) {
		// navigateTo('/auth/login')
		return nuxtApp.runWithContext(() => navigateTo('/auth/login'))
	}
})
