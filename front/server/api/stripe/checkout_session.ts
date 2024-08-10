import Stripe from 'stripe'

export default defineEventHandler(async event => {
	const config = useRuntimeConfig()
	const stripe = new Stripe(
		'sk_test_51PeaLJGPPLiXUX5U62ICn94JszVYsY1N8qRmlqwMPIuumgIe017yhPb4Iaet2wMM3EHOsBjIztsaFUlnLmUUlQ8H00MOoDnPE3'
	)
	const body = await readBody(event)

	try {
		const session = await stripe.checkout.sessions.create({
			customer: body.id_customer,
			cancel_url: 'http://localhost:3000/profile',
			success_url: 'http://localhost:3000/profile',
			line_items: [
				{
					price: body.id_price,
					quantity: 1,
				},
			],
			mode: 'subscription',
		})

		return session
	} catch (error) {
		console.error('Error creating checkout session:', error)
		throw createError({
			statusCode: 500,
			statusMessage: 'Error creating checkout session',
		})
	}
})
