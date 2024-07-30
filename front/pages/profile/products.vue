<template>
	
    <DashboardNavbar
      title="Products"
      v-model="isSidebarOpen"
    />
    
    <div>
      page content
    </div>
  </template>
  
  <script setup lang="ts">
  const {isSidebarOpen} = useDashboard()
  definePageMeta({
      title: 'Products',
      layout: 'profile',
      middleware: ['auth-user'],
  })
  
  </script>