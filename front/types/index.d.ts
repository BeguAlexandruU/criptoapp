export { CookieOptions, Post }
declare global {
	interface Post {
		id: string
		title: string
		description: string
		type: string
		status: number
		created_at: Date
		updated_at: Date
	}

	interface Product {
		id: string
		title: string
		description: string
		price: number
		status: number
		duration: number
		created_at: Date
		updated_at: Date
	}

	interface Wallet {
		status: number
		start_date: string
		end_date: string
		title: string
		description: string
	}

	interface UserApiResponse {
		status: boolean
		data?: any
	}

	interface UserRead {
		id: string
		email: string
		is_active: boolean
		is_superuser: boolean
		is_verified: boolean

		nume: string
		id_stripe_customer: string
		ref_code: string
		ref_code_parent: string

		hashed_password: string
		created_at: string
		updated_at: string
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
