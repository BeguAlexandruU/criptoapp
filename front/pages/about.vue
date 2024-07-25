<template>
  <div class="flex flex-col justify-between h-32">
    <UDropdown :items="items" :popper="{ placement: 'bottom-start' }">
      <UAvatar
          src="https://avatars.githubusercontent.com/u/739984?v=4"
          alt="Avatar"
      />
    </UDropdown>
    Icon
    <UIcon name="i-uiw-logout"/>
  </div>
  
</template>

<script setup lang="ts">
const items = [
  [{
    label: 'Profile',
    avatar: {
      src: 'https://avatars.githubusercontent.com/u/739984?v=4'
    }
  }], [{
    label: 'Logout',
    icon: 'i-uiw-logout',
    click: () => {
      console.log('Logout')
    }
  }]
]
</script>