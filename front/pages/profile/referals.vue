<template>
	<DashboardNavbar title="Referals" v-model="isSidebarOpen" />

	<!-- page content container  -->
	<div class="flex flex-1 flex-col p-4">
		<!-- invite link container -->
		<div class="max-w-fit">
			<div
				class="flex justify-between gap-1.5 px-4 py-3 rounded-t-md border-gray-700 border border-b-0"
			>
				<div class="flex items-center gap-1.5">
					<UIcon name="ic:baseline-link" class="h-5 w-5" />
					<span>Invite link</span>
				</div>

				<UIcon
					name="heroicons:clipboard-document"
					class="text-gray-400 hover:text-white cursor-pointer"
					@click="copyLink"
				/>
			</div>
			<pre
				class="px-4 py-3 bg-gray-800 rounded-b-md border-gray-700 border overflow-x-auto"
			>
http://localhost:3000/auth/register?ref={{ userStore.user.ref_code }}</pre
			>
		</div>
	</div>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
const userStore = useUserStore()
const toast = useToast()

definePageMeta({
	title: 'Referals',
	layout: 'profile',
	middleware: ['auth-user'],
})

function copyLink() {
	navigator.clipboard.writeText(
		'http://localhost:3000/auth/register?ref=' + userStore.user.ref_code
	)
	toast.add({ title: 'Link copied' })
}
</script>
