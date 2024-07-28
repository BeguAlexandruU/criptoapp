import { createSharedComposable, useWindowSize } from '@vueuse/core'

const { width, height } = useWindowSize()

const _useDashboard = () => {
  const route = useRoute()
  const router = useRouter()
  const isHelpSlideoverOpen = ref(false)
  const isNotificationsSlideoverOpen = ref(false)
  const isSidebarOpen = ref(width.value > 768)

  defineShortcuts({
    'g-h': () => router.push('/'),
    'g-i': () => router.push('/profile/inbox'),
  })

  watch(() => route.fullPath, () => {
    isHelpSlideoverOpen.value = false
    isNotificationsSlideoverOpen.value = false
    isSidebarOpen.value = (width.value > 768);
    
  })

  return {
    isHelpSlideoverOpen,
    isNotificationsSlideoverOpen,
    isSidebarOpen
  }
}

export const useDashboard = createSharedComposable(_useDashboard)