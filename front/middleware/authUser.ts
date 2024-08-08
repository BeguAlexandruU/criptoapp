export default defineNuxtRouteMiddleware(async (to, from) => {
	const userStore = useUserStore()

	if (!userStore.user) {
		const router = useRouter()
		// userStore.setRoute(to.fullPath)
		// return router.push({ path: '/auth/login' })
		return navigateTo('/auth/login', { external: true })
	}
})
