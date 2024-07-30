<template>
	
    <DashboardNavbar
      title="Posts"
      v-model="isSidebarOpen"
    />
    
    <div>
      page content
    </div>
  </template>
  
  <script setup lang="ts">
  const {isSidebarOpen} = useDashboard()
  definePageMeta({
      title: 'Posts',
      layout: 'profile',
      middleware: ['auth-user'],
  })
  
  </script>