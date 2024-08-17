<template>
	<div
		v-if="selectedItemId != null"
		class="hidden md:flex flex-col flex-1 gap-2 p-4"
	>
		<slot />
	</div>

	<div
		v-else
		class="hidden md:flex flex-1 justify-center items-center gap-2 p-4"
	>
		<UIcon name="i-heroicons-inbox" class="h-32 w-32 text-gray-600" />
	</div>

	<USlideover v-model="isSideoverItemOpen" class="flex md:hidden">
		<div class="flex flex-col flex-1 gap-2 p-4">
			<slot />
		</div>
	</USlideover>
</template>

<script setup>
const selectedItemId = defineModel('selectedItemId')
const isSideoverItemOpen = defineModel('isSideoverItemOpen')
</script>
