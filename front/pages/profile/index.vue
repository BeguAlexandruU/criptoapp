<template>
	<DashboardNavbar
    	title="Profile"
    	v-model="isSidebarOpen"
  	/>

	<div v-if="status === 'pending'">Loading ...</div>
	<div v-else>
		<div v-for="item in posts">
			<h1>title: {{ item.title }}</h1>
		</div>
	</div>

</template>

<script setup lang="ts">
const {isSidebarOpen} = useDashboard()
definePageMeta({
	title: 'Profile',
	layout: 'profile',
	middleware: ['auth-user'],
})

const { status, data: posts } = await useFetch<Post[]>('/api/posts', {
	lazy: true,
})
</script>
