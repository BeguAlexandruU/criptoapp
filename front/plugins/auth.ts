export default defineNuxtPlugin(async nuxtApp => {
	const userStore = useUserStore()

	if (!userStore.email) {
		await userStore.fetchUser()
	}
})
