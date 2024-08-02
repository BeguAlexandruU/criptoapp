export default defineEventHandler(async data => {
	try {
		const { access_token } = await readBody(data)
		const res = await $fetch('http://localhost:5001/auth/curent_user', {
			method: 'GET',
			headers: {
				accept: 'application/json',
				Authorization: `Bearer ${access_token}`,
			},
			credentials: 'include',
		})
		return res
	} catch (error) {
		console.log(error)
	}
})
