<template>
	<div class="pl-2">
		<pre>{{ $data }}</pre>
	</div>
</template>

<script setup lang="ts">
onMounted(async () => {
	const { data } = await useFetch('/api/posts')
})
</script>
