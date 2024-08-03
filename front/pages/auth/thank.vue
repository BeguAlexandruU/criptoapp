<script setup lang="ts">
definePageMeta({
	title: 'Thank',
	layout: 'auth',
})

const route = useRoute()
const name = route.query.name
</script>

<template>
	<!-- form container  -->
	<div
		class="px-4 py-5 rounded-xl divide-y divide-gray-800 ring-1 ring-gray-800 shadow max-w-sm w-full bg-white/5 backdrop-blur"
	>
		<!-- form header -->
		<div
			class="flex flex-col justify-center gap-8 items-center text-center"
		>
			<UIcon name="heroicons:face-smile" class="h-10 w-10 my-2" />
			<p class="text-2xl font-bold text-white">Thank you for join us!</p>
			<p class="text-2xl font-bold text-white">
				<UIcon name="heroicons:sparkles" class="h-5 w-5" />
				{{ name }}
				<UIcon name="heroicons:sparkles" class="h-5 w-5" />
			</p>

			<UButton
				type="submit"
				class="px-3 py-2 w-full flex justify-center font-bold rounded-full"
				to="/auth/login"
			>
				<span>Continue to login</span>
				<UIcon name="heroicons:chevron-right" class="h-5 w-5" />
			</UButton>
		</div>
	</div>
</template>
