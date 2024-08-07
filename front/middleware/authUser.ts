export default defineNuxtRouteMiddleware(async (to, from) => {
	const userStore = useUserStore()

	if (!userStore.user) {
		return navigateTo('/auth/login')
	}
})
