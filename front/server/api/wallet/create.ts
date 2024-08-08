export default defineEventHandler(async data => {
	try {
		const { access_token, id_product } = await readBody(data)

		const fetch_res = await $fetch('http://localhost:5001/wallet/create', {
			method: 'POST',
			headers: {
				accept: 'application/json',
				Authorization: `Bearer ${access_token}`,
			},
			credentials: 'include',
			body: {
				id_user: '',
				id_product: id_product,
				status: 0,
			},
		})
		const res = await fetch_res
		return res
	} catch (error) {
		console.log(error)
	}
})
