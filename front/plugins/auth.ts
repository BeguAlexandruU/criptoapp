export default defineNuxtPlugin(async nuxtApp => {
	const userStore = useUserStore()

	if (!userStore.user && userStore.accessToken) {
		await userStore.fetchUser()
		await userStore.fetchPosts()
	}
})
