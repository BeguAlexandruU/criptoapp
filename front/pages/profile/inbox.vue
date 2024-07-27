<template>
    <h1>inbox</h1>
</template>

<script setup lang="ts">
definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})

</script>