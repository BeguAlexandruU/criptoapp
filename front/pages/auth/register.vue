<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types'

definePageMeta({
	title: 'Register',
	layout: 'auth',
})

const route = useRoute()

const state = reactive({
	name: undefined,
	email: '',
	password: '',
	conf_password: '',
	ref_code_parent: route.query.ref,
})

const validate = (state: any): FormError[] => {
	const errors = []
	if (!state.name) errors.push({ path: 'name', message: 'Required' })
	if (!state.email) errors.push({ path: 'email', message: 'Required' })
	if (!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(state.email))
		errors.push({ path: 'email', message: 'Enter a valid email' })
	if (!state.password) errors.push({ path: 'password', message: 'Required' })
	if (!state.conf_password)
		errors.push({ path: 'conf_password', message: 'Required' })
	if (state.password != state.conf_password)
		errors.push({ path: 'conf_password', message: 'No match' })
	return errors
}

async function onSubmit(event: FormSubmitEvent<any>) {
	try {
		const res = await $fetch<any>('/api/auth/register', {
			method: 'POST',
			body: event.data,
		})

		if (res)
			await navigateTo(
				{
					path: '/auth/thank',
					query: {
						name: state.name,
					},
				},
				{
					external: true,
				}
			)
	} catch (error: any) {
		console.error(error)
		alert('Erroare')
	}
}
</script>

<template>
	<!-- form container  -->
	<div
		class="px-4 py-5 rounded-xl divide-y divide-gray-800 ring-1 ring-gray-800 shadow max-w-sm w-full bg-white/5 backdrop-blur"
	>
		<!-- form header -->
		<div class="flex flex-col justify-center items-center text-center">
			<UIcon name="heroicons:lock-closed" class="h-10 w-10 my-2" />
			<p class="text-2xl font-bold text-white">Create an accout</p>
			<div class="text-gray-400">
				Already have an account?
				<ULink to="/auth/login" class="text-primary font-medium"
					>Login</ULink
				>
				.
			</div>
		</div>

		<!-- form body -->
		<UForm
			:validate="validate"
			:state="state"
			class="space-y-6 my-6"
			@submit="onSubmit"
		>
			<UFormGroup label="Name" name="name">
				<UInput v-model="state.name" />
			</UFormGroup>

			<UFormGroup label="Email" name="email">
				<UInput v-model="state.email" />
			</UFormGroup>

			<UFormGroup label="Password" name="password">
				<UInput v-model="state.password" type="password" />
			</UFormGroup>

			<UFormGroup label="Confirm password" name="conf_password">
				<UInput v-model="state.conf_password" type="password" />
			</UFormGroup>

			<UButton
				type="submit"
				class="px-3 py-2 w-full flex justify-center font-bold rounded-full"
			>
				<UIcon name="ic:baseline-person-add-alt" class="h-5 w-5" />
				<span>Create account</span>
			</UButton>
		</UForm>
		<!-- form footer -->
		<div></div>
	</div>
</template>
