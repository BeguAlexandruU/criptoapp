// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	compatibilityDate: '2024-04-03',
	devtools: { enabled: true },
	modules: [
		'@nuxt/ui',
		'@pinia/nuxt',
	],
	pinia: {
		storesDirs: ['./stores/**', './custom-folder/stores/**'],
	},
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
