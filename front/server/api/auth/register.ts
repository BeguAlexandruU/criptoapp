export default defineEventHandler(async event => {
	try {
		const data = await readBody(event)

		const res = await $fetch('http://localhost:5001/auth/register', {
			method: 'POST',
			headers: {
				accept: 'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(data),
		})

		return res
	} catch (error: any) {
		return error
	}
})
