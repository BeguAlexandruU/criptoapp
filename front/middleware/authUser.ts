export default defineNuxtRouteMiddleware(async (to, from) => {

	// const nuxtApp = useNuxtApp()

	// const res:UserApiResponse = await $fetch('/api/auth/curent_user')

	// if(!res.status){
	// 	//navigateTo('/auth/login')
	// 	return nuxtApp.runWithContext(() => navigateTo('/auth/login'))

	// }

	const token = useCookie('accessToken')

    if (!token.value) {
        return navigateTo('/auth/signin')
    }

})
