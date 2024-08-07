<template>
	<DashboardNavbar title="Wallet" v-model="isSidebarOpen" />
	<!-- page content container  -->
	<div class="flex-1 p-4 overflow-scroll">
		<!-- product list container -->
		<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-8">
			<div
				v-for="item in wallet"
				class="flex flex-col flex-1 gap-1 border-gray-800 border bg-gray-900 rounded-md px-4 py-5"
			>
				<span class="text-3xl font-semibold">{{ item.title }}</span>
				<span class="text-gray-400">{{ item.description }}</span>
				<span class="text-gray-400">Status: {{ item.status }}</span>
				<UDivider />
				<span class="text-gray-400">Start: {{ item.start_date }}</span>
				<span class="text-gray-400">End: {{ item.end_date }}</span>

				<UProgress
					:value="Date.parse(item.end_date) - Date.now()"
					:max="
						Date.parse(item.end_date) - Date.parse(item.start_date)
					"
					indicator
				/>
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
const userStore = useUserStore()
definePageMeta({
	title: 'Wallet',
	layout: 'profile',
	middleware: ['auth-user'],
})

const { status, data: wallet } = await useFetch<Wallet[]>(
	'/api/wallet/get_by_user',
	{
		method: 'POST',
		body: {
			access_token: userStore.accessToken,
		},
	}
)
</script>
