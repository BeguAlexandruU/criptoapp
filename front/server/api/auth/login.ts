export default defineEventHandler(async data => {
	try {
		const { email, password } = await readBody(data)

		const res = await $fetch('http://localhost:5001/auth/jwt/login', {
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
		})

		return res
	} catch (error) {
		console.log(error)
	}
})
