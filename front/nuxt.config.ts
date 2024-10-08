// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	compatibilityDate: '2024-04-03',
	devtools: { enabled: true },
	modules: ['@nuxt/ui', '@pinia/nuxt', '@nuxtjs/tailwindcss'],
	pinia: {
		storesDirs: ['./stores/**', './custom-folder/stores/**'],
	},
	css: ['~/assets/css/tailwind.css'],
	runtimeConfig: {
		secret: {
			STRIPE_SECRET_KEY: process.env.STRIPE_SECRET_KEY,
		},
		public: {
			PORT: process.env.PORT ? parseInt(process.env.PORT, 10) : 4000,
			HOST: process.env.HOST || '0.0.0.0',
		},
	},

	devServer: {
		port: 4000,
		host: '0.0.0.0',
	},
})
