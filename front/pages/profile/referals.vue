<template>
	
    <DashboardNavbar
      title="Referals"
      v-model="isSidebarOpen"
    />
    
    <div>
      page content
    </div>
  </template>
  
  <script setup lang="ts">
  const {isSidebarOpen} = useDashboard()
  definePageMeta({
      title: 'Referals',
      layout: 'profile',
      middleware: ['auth-user'],
  })
  
  </script>