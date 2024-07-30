<template>
    
    <div class="hidden md:flex flex-col w-60 p-4 bg-gray-900 border-r border-gray-800 h-screen">
        <slot/>
    </div>

    <USlideover v-model="isSidebarOpen" side="left">
        <div class="flex flex-col flex-1 h-screen p-4">
            <slot/>
        </div>
    </USlideover>
</template>

<script setup>
const isSidebarOpen = defineModel()

</script>