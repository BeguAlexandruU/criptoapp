// export function setCookie(value: string, options: CookieOptions = {}) {
// 	const name = 'accessToken'
// 	// Set default attributes for "accessToken" cookie

// 	options = {
// 		...options,
// 		SameSite: 'None', // Explicitly define SameSite attribute
// 		Secure: true, // Ensure Secure attribute is set when SameSite=None
// 	}

// 	let updatedCookie =
// 		encodeURIComponent(name) + '=' + encodeURIComponent(value)

// 	for (let optionKey in options) {
// 		updatedCookie += '; ' + optionKey
// 		let optionValue = options[optionKey]
// 		if (optionValue !== true) {
// 			updatedCookie += '=' + optionValue
// 		}
// 	}

// 	document.cookie = updatedCookie
// }

// export function getCookie(name: string): string | undefined {
// 	const value = `; ${document.cookie}`
// 	const parts = value.split(`; ${name}=`)
// 	if (parts.length === 2) return parts.pop()?.split(';').shift()
// }
