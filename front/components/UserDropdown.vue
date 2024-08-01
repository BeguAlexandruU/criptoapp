<script setup lang="ts">
import { useUserStore } from '~/stores/userStore'

const { isHelpSlideoverOpen } = useDashboard()
const { metaSymbol } = useShortcuts()

const userStore = useUserStore()

const items = computed(() => [
  [{
    slot: 'account',
    label: '',
    disabled: true
  },{
    label: 'Accout settings',
    icon: 'i-heroicons-cog-8-tooth'
    }],[{
    label: 'Sign out',
    icon: 'i-heroicons-arrow-left-on-rectangle',
    click: async () => {
      await $fetch('/api/auth/logout')
      navigateTo('/auth/login')
    }
  }]
])
</script>

<template>
  <UDropdown
    mode="hover"
    :items="items"
    :ui="{ width: 'w-full', item: { disabled: 'cursor-text select-text' } }"
    :popper="{ strategy: 'absolute', placement: 'top' }"
    class="w-full"
  >
    <template #default="{ open }">
      <UButton
        color="gray"
        variant="ghost"
        class="w-full"
        :label=userStore.name
        :class="[open && 'bg-gray-50 dark:bg-gray-800']"
      >
        <template #leading>
          <UAvatar
            src="https://avatars.githubusercontent.com/u/739984?v=4"
            size="2xs"
          />
        </template>

        <template #trailing>
          <UIcon
            name="i-heroicons-ellipsis-vertical"
            class="w-5 h-5 ml-auto"
          />
        </template>
      </UButton>
    </template>

    <template #account>
      <div class="text-left">
        <p>
          Signed in as
        </p>
        <p class="truncate font-medium text-gray-900 dark:text-white">
          {{userStore.email}}
        </p>
      </div>
    </template>
  </UDropdown>
</template>