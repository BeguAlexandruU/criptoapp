<template>
	<DashboardNavbar title="Posts" v-model="isSidebarOpen" />

	<!-- page content container  -->
	<div class="flex-1 p-4 overflow-y-auto">
		<!-- product list container -->
		<div class="grid gap-4">
			<div
				v-for="item in posts"
				class="flex flex-col flex-1 gap-1 border-gray-800 border bg-gray-900 rounded-md px-4 py-5"
				@click="
					() => {
						sideoverPostId = posts.indexOf(item)
						isSideoverOpen = true
					}
				"
			>
				<span class="text-3xl font-semibold">{{ item.title }}</span>
				<span class="text-gray-400">{{ item.description }}</span>
			</div>
		</div>
	</div>

	<!-- sideover -->
	<USlideover v-model="isSideoverOpen">
		<UCard
			class="flex flex-col flex-1"
			:ui="{
				body: { base: 'flex-1' },
				ring: '',
				divide: 'divide-y divide-gray-100 dark:divide-gray-800',
			}"
		>
			<template #header>
				<UButton
					color="gray"
					variant="ghost"
					size="sm"
					icon="i-heroicons-x-mark-20-solid"
					class="flex sm:hidden absolute end-5 top-5 z-10"
					square
					padded
					@click="isSideoverOpen = false"
				/>

				<div>
					<span class="text-3xl font-semibold">{{
						posts[sideoverPostId].title
					}}</span>
				</div>
			</template>

			<div>
				<span class="text-gray-400">{{
					posts[sideoverPostId].description
				}}</span>
			</div>

			<template #footer>
				<!-- <Placeholder class="h-8" /> -->
			</template>
		</UCard>
	</USlideover>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
definePageMeta({
	title: 'Posts',
	layout: 'profile',
	middleware: ['auth-user'],
})
const isSideoverOpen = ref(false)
const sideoverPostId = ref(0)
const posts = ref<Post[]>([])
const userStore = useUserStore()
onMounted(() => {
	const socket = new WebSocket(
		'ws://localhost:5001/ws/post?token=' + userStore.accessToken
	)
	socket.addEventListener('open', event => {
		console.log('Connected to WS Server')
		socket.send('getPosts')
	})

	socket.addEventListener('message', event => {
		console.log(JSON.parse(event.data))
		posts.value.push(JSON.parse(event.data))
	})

	socket.addEventListener('error', error => {
		console.log('Error: ', error)
	})
})
</script>
