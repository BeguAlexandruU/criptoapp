<script setup lang="ts">

const route = useRoute()
const appConfig = useAppConfig()
const { isHelpSlideoverOpen, isSidebarOpen } = useDashboard()

const links = [{
  id: 'profile',
  label: 'Profile',
  icon: 'i-heroicons-user',
  to: '/profile',
}, {
  id: 'inbox',
  label: 'Inbox',
  icon: 'i-heroicons-inbox',
  to: '/profile/inbox',
  badge: '0',
}, {
  id: 'posts',
  label: 'Posts',
  to: '/profile/posts',
  icon: 'heroicons:newspaper',
}, {
  id: 'products',
  label: 'Products',
  icon: 'heroicons:shopping-cart',
  to: '/profile/products',
}, {
  id: 'referals',
  label: 'Referals',
  icon: 'i-heroicons-user-group',
  to: '/profile/referals',
}]

const footerLinks = [{
  label: 'Invite people',
  icon: 'i-heroicons-plus',
  to: '/profile/referals'
}, {
  label: 'Help & Support',
  icon: 'i-heroicons-question-mark-circle',
  click: () => isHelpSlideoverOpen.value = true
}]



// const defaultColors = ref(['green', 'teal', 'cyan', 'sky', 'blue', 'indigo', 'violet'].map(color => ({ label: color, chip: color, click: () => appConfig.ui.primary = color })))
// const colors = computed(() => defaultColors.value.map(color => ({ ...color, active: appConfig.ui.primary === color.label })))
</script>

<template>
  
  <!-- layout container -->
  <div class="flex w-screen h-screen bg-gray-900">
    <!-- sidebar container -->
    <DashboardSidebar v-model="isSidebarOpen">
      <!-- navbar -->
      <div class="flex items-stretch gap-1.5">
        <UButton
            icon="material-symbols:menu-rounded"
            size="sm"
            square
            color="gray"
            variant="ghost"
            class="block md:hidden m-r-3"
            @click= "()=>{
              isSidebarOpen=!isSidebarOpen;
            }"
          />
          <UButton
            color="gray"
            variant="ghost"
            class="flex-1"
            to="/"
          >
            <UAvatar
              src="https://avatars.githubusercontent.com/u/23360933?s=200&v=4"
              size="2xs"
            /> 
            <span class="truncate text-gray-900 dark:text-white font-semibold">Cripro app</span>
          </UButton>
          
      </div>

      <!-- sidebar container -->
      <div class="flex flex-col flex-1 overflow-scroll">

        <UVerticalNavigation :links="links" />

        <UDivider />

        <div class="flex-1"/>

        <UVerticalNavigation :links="footerLinks" />
      </div>

      <!-- user dropdown -->
      <div >
        <UDivider/>
        <!-- ~/components/UserDropdown.vue -->
        <UserDropdown />
      </div>
    </DashboardSidebar>

    <!-- content page -->
    <div class="flex flex-col w-full h-screen">
      <slot />
    </div>

  </div>
</template>