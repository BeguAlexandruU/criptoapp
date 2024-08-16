export default defineEventHandler(async data => {
	try {
		const { access_token } = await readBody(data)
		const fetch_res = await $fetch(
			'http://localhost:5001/notification/user',
			{
				method: 'GET',
				headers: {
					accept: 'application/json',
					Authorization: `Bearer ${access_token}`,
				},
				credentials: 'include',
			}
		)
		const res = await fetch_res
		return res
	} catch (error) {
		console.log(error)
	}
})
