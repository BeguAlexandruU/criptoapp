<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types'

definePageMeta({
	title: 'Login',
	layout: 'auth',
})

const state = reactive({
	email: undefined,
	password: undefined,
})

const validate = (state: any): FormError[] => {
	const errors = []
	if (!state.email) errors.push({ path: 'email', message: 'Required' })
	if (!state.password) errors.push({ path: 'password', message: 'Required' })
	return errors
}

const userStore = useUserStore()

async function onSubmit(event: FormSubmitEvent<any>) {
	await userStore.signIn(event.data)

	await navigateTo('/profile', { external: true })
}

definePageMeta({
	title: 'Inbox',
	layout: 'profile',
})
</script>

<template>
	<UForm
		:validate="validate"
		:state="state"
		class="space-y-4"
		@submit="onSubmit"
	>
		<UFormGroup label="Email" name="email">
			<UInput v-model="state.email" />
		</UFormGroup>

		<UFormGroup label="Password" name="password">
			<UInput v-model="state.password" type="password" />
		</UFormGroup>

		<UButton type="submit"> Submit </UButton>
	</UForm>
</template>
