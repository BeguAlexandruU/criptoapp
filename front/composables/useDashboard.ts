import { createSharedComposable } from '@vueuse/core'

const _useDashboard = () => {
	const route = useRoute()
	const router = useRouter()
	const isHelpSlideoverOpen = ref(false)
	const isNotificationsSlideoverOpen = ref(false)
	const isSidebarOpen = ref(false)

	defineShortcuts({
		'g-h': () => router.push('/'),
		'g-i': () => router.push('/profile/inbox'),
	})

	watch(
		() => route.fullPath,
		() => {
			isHelpSlideoverOpen.value = false
			isNotificationsSlideoverOpen.value = false
			isSidebarOpen.value = false
		}
	)

	return {
		isHelpSlideoverOpen,
		isNotificationsSlideoverOpen,
		isSidebarOpen,
	}
}

export const useDashboard = createSharedComposable(_useDashboard)
