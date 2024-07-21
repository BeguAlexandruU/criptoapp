export default defineEventHandler(async event => {
	const response = await fetch('http://localhost:5001/post/all')
	const posts = await response.json()
	return posts
})
