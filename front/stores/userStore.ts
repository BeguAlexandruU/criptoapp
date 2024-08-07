import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
	// arrow function recommended for full type inference
	const user = ref()

	const accessToken = useCookie('accessToken', {
		maxAge: 60 * 60,
	})

	const setToken = (data?: string) => (accessToken.value = data)
	const setUser = (data?: UserRead) => (user.value = data)

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
		} catch (error) {
			setToken()
			setUser()
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
			console.log(error)
		}
	}

	const logout = () => {
		setToken()
		setUser()
	}

	return {
		user,
		accessToken,
		logout,
		signIn,
		fetchUser,
		setUser,
		setToken,
	}
})
