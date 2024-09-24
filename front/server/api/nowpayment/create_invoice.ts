export default defineEventHandler(async data => {
	try {
		const { access_token, id_product } = await readBody(data)

		const fetch_res = await $fetch(
			'http://localhost:5001/nowpayment/invoice/create',
			{
				method: 'POST',
				headers: {
					accept: 'application/json',
					Authorization: `Bearer ${access_token}`,
				},
				credentials: 'include',
				body: JSON.stringify({
					product_id: id_product,
				}),
			}
		)
		const res = (await fetch_res) as InvoiceResponse
		return { invoice_url: res.invoice_url }
	} catch (error) {
		console.log(error)
	}
})
