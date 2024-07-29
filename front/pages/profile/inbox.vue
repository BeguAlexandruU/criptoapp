<template>
	
  <DashboardNavbar
    title="Inbox"
    v-model="isSidebarOpen"
  />
  
  <div>
    page content
  </div>
</template>

<script setup lang="ts">
const {isSidebarOpen} = useDashboard()
definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})

</script>