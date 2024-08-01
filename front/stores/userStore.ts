import { defineStore } from 'pinia'

export const useUserStore = defineStore('storeId', {
  // arrow function recommended for full type inference
  state: () => {
    return {
      email: 'default@email.com',
      name: 'default',
    }
  },
})