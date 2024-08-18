<template>
	<DashboardNavbar title="Inbox" v-model="isSidebarOpen" />

	<!-- page content container  -->
	<div class="flex flex-1 flex-row overflow-auto">
		<!-- notifications list container -->
		<div class="flex-1 border-r border-gray-800 overflow-y-auto">
			<div class="flex flex-col-reverse">
				<div
					v-for="item in notificationStore.notifications"
					class="flex flex-col"
					@click="
						() => {
							selectedNotificationId =
								notificationStore.notifications.indexOf(item)

							isSideoverNotificationOpen = true
						}
					"
				>
					<div
						v-if="
							notificationStore.notifications.indexOf(item) ==
							selectedNotificationId
						"
						class="flex flex-col flex-1 gap-1 border-l-2 border-gray-700 hover:border-gray-600 bg-gray-800 hover:bg-gray-700 px-3 py-4"
					>
						<span class="text-xl font-semibold">{{
							item.title
						}}</span>
						<span class="text-gray-400">{{ item.message }}</span>
						<span class="text-gray-400">{{
							getItemHour(item)
						}}</span>
						<span class="text-gray-400">{{
							getItemDate(item)
						}}</span>
					</div>
					<div
						v-else
						class="flex flex-col flex-1 gap-1 border-l-2 border-gray-900 hover:border-gray-600 bg-gray-900 hover:bg-gray-700 px-3 py-4"
					>
						<span class="text-xl font-semibold">{{
							item.title
						}}</span>
						<span class="text-gray-400">{{ item.message }}</span>
						<span class="text-gray-400">{{
							getItemHour(item)
						}}</span>
						<span class="text-gray-400">{{
							getItemDate(item)
						}}</span>
					</div>
					<UDivider />
				</div>
			</div>
		</div>

		<!-- selected notification container -->
		<DashboardInboxSelectedItem
			v-model:selectedItemId="selectedNotificationId"
			v-model:isSideoverItemOpen="isSideoverNotificationOpen"
		>
			<div class="flex gap-1.5">
				<UButton
					icon="material-symbols:close"
					size="sm"
					square
					color="gray"
					variant="ghost"
					class="block md:hidden m-r-3"
					@click="isSideoverNotificationOpen = false"
				/>
				<span class="text-3xl font-semibold">{{
					notificationStore.notifications[selectedNotificationId]
						?.title
				}}</span>
			</div>
			<UDivider />
			<span class="text-gray-400">{{
				notificationStore.notifications[selectedNotificationId]?.message
			}}</span>
		</DashboardInboxSelectedItem>
	</div>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
const notificationStore = useNotificationStore()

definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})

const isSideoverNotificationOpen = ref(false)
const selectedNotificationId = ref()

const getItemHour = item => {
	let date = new Date(item.created_at)
	return date.getHours() + ':' + date.getMinutes()
}
const getItemDate = item => {
	const month = [
		'January',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December',
	]

	let date = new Date(item.created_at)
	return date.getDate() + ' ' + month[date.getMonth()]
}
</script>
