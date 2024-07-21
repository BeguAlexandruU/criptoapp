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
</template>

<script setup lang="ts">
const { status, data: posts } = await useFetch<Post[]>('/api/posts', {
	lazy: true,
})
</script>
