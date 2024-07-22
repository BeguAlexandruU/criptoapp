<template>
	<UBreadcrumb :links="links">
		<template #icon="{ link }">
			<UIcon :name="link.icon" />
			tsts
		</template>
	</UBreadcrumb>
</template>

<script setup lang="ts">
import type { BreadcrumbLink } from '#ui/types'
definePageMeta({
	title: 'Landing Page',
	layout: 'default',
})

export interface Props {
	links: BreadcrumbLink[]
}

defineProps<Props>()
</script>
