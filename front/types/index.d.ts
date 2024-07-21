export { CookieOptions, Post }
declare global {
	interface Post {
		id: number
		title: string
		description: string
		type: number
		status: number
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
