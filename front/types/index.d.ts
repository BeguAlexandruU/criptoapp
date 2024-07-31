export { CookieOptions, Post }
declare global {
	interface Post {
		id: number
		title: string
		description: string
		type: string
		status: number
		created_at: Date
		updated_at: Date
	}

	interface Product {
		id: number
		title: string
		description: string
		price: number
		status: number
		duration: number
		created_at: Date
		updated_at: Date
	}

	interface CookieOptions {
		SameSite?: 'Lax' | 'Strict' | 'None'
		Secure?: boolean
		[key: string]: string | boolean | undefined
	}

	interface AccessTokenData {
		access_token: string
	}
}
