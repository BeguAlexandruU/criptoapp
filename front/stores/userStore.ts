import { useWebSocket } from '@vueuse/core'
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
	// arrow function recommended for full type inference
	const user = ref()
	const posts = ref<Post[]>([])

	const accessToken = useCookie('accessToken', {
		maxAge: 60 * 60,
	})

	const socketUrl = ref()

	const { open, close, send, status, data } = useWebSocket(
		'ws://localhost:5001/ws/post?token=' + accessToken.value
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

	watch(data, newData => {
		if (newData) {
			const parsedData = JSON.parse(newData)
			console.log(parsedData)
			posts.value.push(parsedData)
		}
	})

	const fetchPosts = async (data?: any) => {
		try {
			open()

			// console.log('fetch posts')
			// if (accessToken.value) {
			// 	console.log('token exist')
			// 	// setSocketUrl()
			// 	setSocketUrl(accessToken.value)
			// } else {
			// 	console.error('Access token is null or undefined')
			// 	return
			// }

			//get user fetch data
			// const socket = new WebSocket(
			// 	'ws://localhost:5001/ws/post?token=' + accessToken.value
			// )
			// socket.addEventListener('open', event => {
			// 	console.log('Connected to WS Server')
			// 	socket.send('getPosts')
			// })
			// socket.addEventListener('message', event => {
			// 	console.log(JSON.parse(event.data))
			// 	posts.value.push(JSON.parse(event.data))
			// })
			// socket.addEventListener('error', error => {
			// 	console.log('Error: ', error)
			// })
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
