export const getPosts = async () => {
	const response = await fetch('http://localhost:5001/post/all')
	const post = await response.json()
	return post
}
