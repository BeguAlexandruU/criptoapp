<template>
	<DashboardNavbar title="Subscriptions" v-model="isSidebarOpen" />
	<!-- page content container  -->
	<div class="flex-1 p-4 overflow-y-auto">
		<!-- product list container -->
		<div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-8">
			<div
				v-for="item in products"
				class="flex flex-col flex-1 gap-1 border-gray-800 border bg-gray-900 rounded-md px-4 py-5"
			>
				<span class="text-3xl font-semibold">{{ item.title }}</span>
				<span class="text-gray-400">{{ item.description }}</span>
				<UDivider />
				<span class="text-gray-400 text-xs"
					>Duration: {{ item.duration }} days</span
				>
				<span class="text-3xl">{{ item.price }}$</span>
				<UButton label="Buy now" @click="buyProduct(item.id)" />
			</div>
		</div>
	</div>
</template>

<script setup lang="ts">
const { isSidebarOpen } = useDashboard()
definePageMeta({
	title: 'Products',
	layout: 'profile',
	middleware: ['auth-user'],
})
const toast = useToast()

const { status, data: products } = await useFetch<Product[]>(
	'/api/product/all',
	{
		lazy: true,
	}
)
async function buyProduct(id_product: string) {
	// const userStore = useUserStore()

	const res = await $fetch('/api/nowpayment/create_invoice', {
		method: 'POST',
		body: {
			access_token: useUserStore().accessToken,
			id_product: id_product,
		},
	})
	if (res?.invoice_url) {
		navigateTo(res.invoice_url, { external: true })
	} else {
		toast.add({
			title: 'Error report',
			description: 'Error creating checkout session',
		})
	}

	// const res = await $fetch('/api/stripe/checkout_session', {
	// 	method: 'POST',
	// 	body: {
	// 		id_customer: userStore.user.id_stripe_customer,
	// 		id_price: id_price,
	// 	},
	// })
	// if (res?.url) {
	// 	navigateTo(res.url, { external: true })
	// } else {
	// 	toast.add({
	// 		title: 'Error report',
	// 		description: 'Error creating checkout session',
	// 	})
	// }
	// const res = await $fetch('/api/wallet/create', {
	// 	method: 'POST',
	// 	body: {
	// 		access_token: userStore.accessToken,
	// 		id_product: id,
	// 	},
	// })
	// if (res) {
	// 	toast.add({
	// 		title: 'Subscribtion completed',
	// 		description: 'You can check your subscrition in wallet',
	// 	})
	// } else {
	// 	alert(res)
	// }
}
</script>
