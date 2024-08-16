<template>
	<DashboardNavbar title="Inbox" v-model="isSidebarOpen" />

	<div>
		<h1>Inbox</h1>
		<ul>
			<li v-for="obj in notificationStore.notifications">
				{{ obj.title }}
			</li>
		</ul>
	</div>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
const notificationStore = useNotificationStore()

definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})
</script>
