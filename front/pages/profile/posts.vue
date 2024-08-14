<template>
	<DashboardNavbar title="Posts" v-model="isSidebarOpen" />

	<div>page content</div>

	<div v-for="item in posts">
		<h1>title: {{ item.title }}</h1>
	</div>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
definePageMeta({
	title: 'Posts',
	layout: 'profile',
	middleware: ['auth-user'],
})

const posts = ref<Post[]>([])
onMounted(() => {
	const socket = new WebSocket('ws://localhost:5001/ws/post')
	socket.addEventListener('open', event => {
		console.log('Connected to WS Server')
	})

	socket.addEventListener('message', event => {
		console.log(JSON.parse(event.data))
		posts.value.push(JSON.parse(event.data))
	})

	socket.addEventListener('error', error => {
		console.log('Error: ', error)
	})
})
</script>
