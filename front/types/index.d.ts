export { Post }
declare global {
	interface Post {
		id: number
		title: string
		description: string
		type: number
		status: number
	}
}
