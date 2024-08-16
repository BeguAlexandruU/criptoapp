export default defineNuxtPlugin(async nuxtApp => {
	const userStore = useUserStore()
	const postStore = usePostStore()
	const notificationStore = useNotificationStore()

	if (!userStore.user && userStore.accessToken) {
		await userStore.fetchUser()
		await postStore.fetchPosts()
		await notificationStore.fetchNotification()
	}
})
