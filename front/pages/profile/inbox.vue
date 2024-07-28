<template>
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
    <h1>inbox</h1>
</template>

<script setup lang="ts">
const {isSidebarOpen } = useDashboard()
definePageMeta({
	title: 'Inbox',
	layout: 'profile',
	middleware: ['auth-user'],
})

</script>