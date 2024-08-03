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
</script>

<template>
	<!-- form container  -->
	<div
		class="px-4 py-5 rounded-xl divide-y divide-gray-800 ring-1 ring-gray-800 shadow max-w-sm w-full bg-white/5 backdrop-blur"
	>
		<!-- form header -->
		<div class="flex flex-col justify-center items-center text-center">
			<UIcon name="heroicons:lock-closed" class="h-10 w-10 my-2" />
			<p class="text-2xl font-bold text-white">Welcome back</p>
			<div class="text-gray-400">
				Don't have an accaunt?
				<ULink to="/auth/register" class="text-primary font-medium"
					>Sign up</ULink
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
			<UFormGroup label="Email" name="email">
				<UInput v-model="state.email" />
			</UFormGroup>

			<UFormGroup label="Password" name="password">
				<template #hint>
					<ULink
						to="/auth/forgotpass"
						class="text-primary font-medium"
						>Forgot password?</ULink
					>
				</template>
				<template #default>
					<UInput v-model="state.password" type="password" />
				</template>
			</UFormGroup>

			<UButton
				type="submit"
				class="px-3 py-2 w-full flex justify-center font-bold rounded-full"
			>
				<UIcon name="ic:baseline-login" class="h-5 w-5" />
				<span>Login</span>
			</UButton>
		</UForm>
		<!-- form footer -->
		<div></div>
	</div>
</template>
