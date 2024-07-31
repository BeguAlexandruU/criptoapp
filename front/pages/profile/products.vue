<template>
    <DashboardNavbar
      title="Products"
      v-model="isSidebarOpen"
    />
    <!-- page content container  -->
    <div class="flex-1 p-4 overflow-scroll">

        <!-- product list container -->
      <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-3 gap-8 ">
        <div v-for="item in products" class="flex flex-col flex-1 gap-1 border-gray-800 border bg-gray-900 rounded-md px-4 py-5" >
          <span class="text-3xl font-semibold">{{ item.title }}</span>
          <span class="text-gray-400">{{ item.description }}</span>
          <UDivider/>
          <span class="text-gray-400 text-xs">Duration: {{ item.duration }}</span>
          <span class="text-3xl">{{ item.price }}$</span>
          <UButton label="Buy now"/>
        </div>
      </div>

      
    </div>
  </template>
  
  <script setup lang="ts">
  const {isSidebarOpen} = useDashboard()
  definePageMeta({
      title: 'Products',
      layout: 'profile',
      middleware: ['auth-user'],
  })


  const { status, data: products } = await useFetch<Product[]>('/api/product/all', {
    lazy: true,
  })
  
  </script>