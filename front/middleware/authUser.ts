export default defineNuxtRouteMiddleware(async (to, from) => {

	const nuxtApp = useNuxtApp()

	const res = await $fetch('/api/auth/curent_user')

	if(res.status){

		console.log(res.data)
	}else{
		//navigateTo('/auth/login')
		return nuxtApp.runWithContext(() => navigateTo('/auth/login'))

	}

})
