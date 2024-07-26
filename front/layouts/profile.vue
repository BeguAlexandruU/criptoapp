<template>
	<UDashboardLayout>
	  <UDashboardPanel>
		<UDashboardNavbar />
  
		<UDashboardSidebar>
		  <template #header>
			<!-- Place anything you like here -->
			<UDashboardSearchButton />
			<UDashboardSidebarLinks :links="links" />
		  </template>
  
		  <UDashboardSidebarLinks />
  
		  <UDivider />
  
		  <UDashboardSidebarLinks />
  
		  <template #footer>
			<!-- Place anything you like here -->
		  </template>
		</UDashboardSidebar>
	  </UDashboardPanel>
  
	  <slot />
	</UDashboardLayout>
  </template>

<script setup lang="ts">
const links = [{
  label: 'Home',
  icon: 'i-heroicons-home',
  tooltip: {
    text: 'Home',
    shortcuts: ['G', 'H']
  }
}, {
  label: 'Inbox',
  icon: 'i-heroicons-inbox',
  badge: '4',
  tooltip: {
    text: 'Inbox',
    shortcuts: ['G', 'I']
  }
}, {
  label: 'Users',
  icon: 'i-heroicons-user-group',
  tooltip: {
    text: 'Users',
    shortcuts: ['G', 'U']
  }
}, {
  label: 'Settings',
  icon: 'i-heroicons-cog-8-tooth',
  children: [{
    label: 'General'
  }, {
    label: 'Members'
  }, {
    label: 'Notifications'
  }],
  tooltip: {
    text: 'Settings',
    shortcuts: ['G', 'S']
  }
}]
</script>