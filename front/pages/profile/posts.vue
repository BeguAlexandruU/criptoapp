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

const { status, data: posts } = await useFetch<Post[]>('/api/posts', {
	lazy: true,
})
</script>
