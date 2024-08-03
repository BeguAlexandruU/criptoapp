<template>
	<DashboardNavbar title="Referals" v-model="isSidebarOpen" />

	<div class="flex border-separate">
		<div>
			<p>My referal code:</p>
			<p>Parent referal code:</p>
		</div>
		<div>
			<p>{{ userStore.user.ref_code }}</p>
			<p>{{ userStore.user.ref_code_parent }}</p>
		</div>
	</div>
	<UButton @click="copyLink"> Copy invite link </UButton>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
const userStore = useUserStore()

definePageMeta({
	title: 'Referals',
	layout: 'profile',
	middleware: ['auth-user'],
})

function copyLink() {
	navigator.clipboard.writeText(
		'http://localhost:3000/auth/register?ref=' + userStore.user.ref_code
	)
}
</script>
