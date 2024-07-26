<script setup lang="ts">
const links = [{
  label: 'Home',
  icon: 'i-heroicons-home'
}, {
  label: 'Inbox',
  icon: 'i-heroicons-inbox',
  badge: '4'
}, {
  label: 'Users',
  icon: 'i-heroicons-user-group'
}, {
  label: 'Settings',
  icon: 'i-heroicons-cog-8-tooth',
  children: [{
    label: 'General'
  }, {
    label: 'Members'
  }, {
    label: 'Notifications'
  }]
}]
</script>

<template>
  <UDashboardPanel class="bg-white" :width="300" :resizable="{ min: 200, max: 400 }">

    <UDashboardSidebar>
      <UDashboardSidebarLinks :links="links" />
    </UDashboardSidebar>
  </UDashboardPanel>
</template>