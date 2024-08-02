export default defineNuxtRouteMiddleware(async (to, from) => {

	const userStore = useUserStore()

    if (!userStore.accessToken) {
        return await navigateTo('/auth/login')
    }

})
