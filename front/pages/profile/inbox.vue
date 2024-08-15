<template>
	<DashboardNavbar title="Inbox" v-model="isSidebarOpen" />

	<div>
		<h1>Inbox</h1>
		<ul>
			<li v-for="obj in data">
				{{ obj.title }}
			</li>
		</ul>
	</div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
const { isSidebarOpen } = useDashboard()

definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})

const data = ref<Post[]>([])
onMounted(() => {
	const socket = new WebSocket('ws://localhost:5001/ws/notification')
	socket.addEventListener('open', event => {
		console.log('Connected to WS Server')
	})

	socket.addEventListener('message', event => {
		console.log(JSON.parse(event.data))
		data.value.push(JSON.parse(event.data))
	})

	socket.addEventListener('error', error => {
		console.log('Error: ', error)
	})
})
</script>
