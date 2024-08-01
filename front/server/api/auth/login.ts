import { useUserStore } from "~/stores/userStore"

export default defineEventHandler(async event => {
	try {

		const { email, password } = await readBody(event)
		const response: Response = await fetch(
			'http://localhost:5001/auth/jwt/login',
			{
				method: 'POST',
				headers: {
					accept: 'application/json',
					'Content-Type': 'application/x-www-form-urlencoded',
				},
				body: `grant_type=&username=${encodeURIComponent(
					email
				)}&password=${encodeURIComponent(
					password
				)}&scope=&client_id=&client_secret=`,
				credentials: 'include',
			}
		)

		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`)
		}

		//set cookie
		const d = new Date()
		d.setTime(d.getTime() + 1 * 60 * 60 * 24 * 1000)
		const data: AccessTokenData = await response.json()
		const access_token: string = data.access_token

		setCookie(event, 'accessToken', access_token, {
			sameSite: 'none',
			secure: true,
			path: '/',
			expires: d,
		})
		
		//set get user data
		const userStore = useUserStore()

		const curent_user_res = await fetch('http://localhost:5001/auth/curent_user', {
            method: 'GET',
            headers: {
                accept: 'application/json',
                Authorization: `Bearer ${access_token}`,
            },
            credentials: 'include',
        })
        const curent_user = await curent_user_res.json()
		const parsed_user = JSON.parse(curent_user)

		//set user data in store
        if(curent_user.detail){
            return { status: false }
        }else{
			userStore.name = parsed_user.name
			userStore.email = parsed_user.email
		}

		return { status: true}
	} catch (error) {
		return { status: false }
	}
})
