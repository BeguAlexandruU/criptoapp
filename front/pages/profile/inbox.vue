<template>
	<DashboardNavbar title="Inbox" v-model="isSidebarOpen" />

	<div>
		<h1>Inbox</h1>
		<ul>
			<li v-for="(message, index) in data" :key="index">
				{{ message }}
			</li>
		</ul>
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
const { isSidebarOpen } = useDashboard()

definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})

const data = ref<string[]>([])
const socket = new WebSocket('ws://localhost:5001/notify/ws')
onMounted(() => {
	socket.addEventListener('open', event => {
		console.log('Connected to WS Server')
	})

	socket.addEventListener('message', event => {
		console.log('Message from WS Server', event.data)
		data.value.push(event.data)
	})

	// Send message to WS Server

	socket.addEventListener('error', error => {
		console.log('Error: ', error)
	})
})
</script>
