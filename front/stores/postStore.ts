import { useWebSocket } from '@vueuse/core'
import { defineStore } from 'pinia'

export const usePostStore = defineStore('post', () => {
	// arrow function recommended for full type inference
	const posts = ref<Post[]>([])
	const toast = useToast()

	const { open, close, send, status, data } = useWebSocket(
		'ws://localhost:5001/ws/post?token=' + useUserStore().accessToken,
		{
			onMessage: (ws, event) => {
				if (event.data) {
					const parsedData = JSON.parse(event.data)
					if (!parsedData.message) {
						posts.value.push(parsedData)
						toast.add({ title: 'New Post' })
					}
				}
			},
		}
	)

	const setPosts = (data: Post[]) => (posts.value = data)

	const fetchPosts = async () => {
		try {
			//get user fetch data
			const res = await $fetch<any>('/api/posts', {
				method: 'GET',
				body: {
					access_token: useUserStore().accessToken,
				},
			})
			setPosts(res)
			open()
		} catch (error) {
			setPosts([])
			console.log(error)
		}
	}

	const reset = () => {
		close()
		setPosts([])
	}

	return {
		posts,
		reset,
		fetchPosts,
	}
})
