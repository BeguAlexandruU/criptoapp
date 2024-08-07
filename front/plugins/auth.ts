export default defineNuxtPlugin(async nuxtApp => {
	const userStore = useUserStore()

	if (!userStore.user) {
		await userStore.fetchUser()
	}
})
