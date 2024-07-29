<template>
    <div class="flex justify-between items-center flex-1 h-16 px-4 border-gray-800 border-b">
        <div class="flex gap-1.5">
            <UButton
                icon="material-symbols:menu-rounded"
                size="sm"
                square
                color="gray"
                variant="ghost"
                class="block md:hidden m-r-3"
                @click= "sidebarChangeState"
            />
            <h1 class="flex items-center font-semibold truncate">
                {{ props.title }}
            </h1>
        </div>
        
        <div>
            <slot/>
        </div>
    </div>
</template>

<script setup>
const props = defineProps({
    title: String
})
    
const isSidebarOpen = defineModel()

function sidebarChangeState() {
    isSidebarOpen.value = !isSidebarOpen.value
}

</script>