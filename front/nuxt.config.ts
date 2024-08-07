// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	compatibilityDate: '2024-04-03',
	devtools: { enabled: true },
	modules: ['@nuxt/ui', '@pinia/nuxt', '@nuxtjs/tailwindcss'],
	pinia: {
		storesDirs: ['./stores/**', './custom-folder/stores/**'],
	},
	css: ['~/assets/css/tailwind.css'],
	// tailwindcss: {
	// 	cssPath: ['~/assets/css/tailwind.css', { injectPosition: 'last' }],
	// 	configPath: 'tailwind.config.js',
	// 	exposeConfig: {
	// 		level: 2,
	// 	},
	// 	config: {},
	// 	viewer: true,
	// },
})
