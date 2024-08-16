import { useWebSocket } from '@vueuse/core'
import { defineStore } from 'pinia'

export const useNotificationStore = defineStore('notification', () => {
	// arrow function recommended for full type inference
	const notifications = ref<Notification[]>([])
	const toast = useToast()

	const { open, close, send, status, data } = useWebSocket(
		'ws://localhost:5001/ws/notification?token=' +
			useUserStore().accessToken,
		{
			onMessage: (ws, event) => {
				if (event.data) {
					const parsedData = JSON.parse(event.data)
					if (!parsedData.message) {
						notifications.value.push(parsedData)
						toast.add({ title: 'New Notification' })
					}
				}
			},
		}
	)

	const setNotifications = (data: Notification[]) =>
		(notifications.value = data)

	const fetchNotification = async () => {
		try {
			//get user fetch data
			const res = await $fetch<any>('/api/notification/get_by_user', {
				method: 'POST',
				body: {
					access_token: useUserStore().accessToken,
				},
			})
			setNotifications(res)
			open()
		} catch (error) {
			setNotifications([])
			console.log(error)
		}
	}

	const reset = () => {
		close()
		setNotifications([])
	}

	return {
		notifications,
		reset,
		fetchNotification,
	}
})
