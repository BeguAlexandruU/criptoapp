<template>
	<div class="pl-2">
		<h2>home page</h2>
	</div>

	<div v-if="status === 'pending'">Loading ...</div>
	<div v-else>
		<div v-for="item in posts">
			<h1>title: {{ item.title }}</h1>
		</div>
	</div>

	<UButton
		@click="logout"
		class="bg-green-200 hover:bg-greeb-500 text-black font-bold py-2 px-4 rounded"
	>
		Logout
	</UButton>
</template>

<script setup lang="ts">
definePageMeta({
	title: 'Home',
	layout: 'default',
	middleware: ['auth-user'],
})

const logout = async () => {
	// @ts-ignore
	await $fetch('/api/logout')
	navigateTo('/login')
}

const { status, data: posts } = await useFetch<Post[]>('/api/posts', {
	lazy: true,
})
</script>
