import { useWebSocket } from '@vueuse/core'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
	// arrow function recommended for full type inference
	const user = ref()
	const posts = ref<Post[]>([])
	const toast = useToast()

	const accessToken = useCookie('accessToken', {
		maxAge: 60 * 60,
	})

	const socketUrl = ref()

	const { open, close, send, status, data } = useWebSocket(
		'ws://localhost:5001/ws/post?token=' + accessToken.value,
		{
			onMessage: (ws, event) => {
				console.log(event)
				if (event.data) {
					const parsedData = JSON.parse(event.data)
					posts.value.push(parsedData)
					if (accessToken.value) {
						toast.add({ title: 'New Post' })
					}
				}
			},
		}
	)

	const setToken = (data?: string) => (accessToken.value = data)
	const setUser = (data?: UserRead) => (user.value = data)
	const setPosts = (data: Post[]) => (posts.value = data)
	const setSocketUrl = (data?: string) =>
		(socketUrl.value = 'ws://localhost:5001/ws/post?token=' + data)

	const signIn = async (data?: any) => {
		try {
			const res = await $fetch<any>('/api/auth/login', {
				method: 'POST',
				body: {
					email: data.email,
					password: data.password,
				},
			})

			setToken(res.access_token)

			await fetchUser()
			await fetchPosts()
		} catch (error) {
			setToken()
			setUser()
			setPosts([])
			console.log(error)
		}
	}

	const fetchUser = async (data?: any) => {
		try {
			//get user fetch data
			const res = await $fetch<any>('/api/auth/curent_user', {
				method: 'POST',
				body: {
					access_token: accessToken.value,
				},
			})

			setUser(res)
		} catch (error) {
			setToken()
			setUser()
			setPosts([])
			console.log(error)
		}
	}

	watch(status, newStatus => {
		if (newStatus === 'OPEN') {
			console.log('Connected to WS Server')
			send('getPosts')
		}
	})

	const fetchPosts = async (data?: any) => {
		try {
			//get user fetch data
			const res = await $fetch<any>('/api/posts', {
				method: 'GET',
				body: {
					access_token: accessToken.value,
				},
			})
			setPosts(res)
			open()
		} catch (error) {
			setPosts([])
			console.log(error)
		}
	}

	const logout = () => {
		setToken()
		setUser()
		setPosts([])
		setSocketUrl()
	}

	return {
		status,
		user,
		accessToken,
		posts,
		logout,
		signIn,
		fetchUser,
		fetchPosts,
		setUser,
		setToken,
	}
})
