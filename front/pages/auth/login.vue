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

async function onSubmit(event: FormSubmitEvent<any>) {
	// Do something with data
	try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(event.data),
        })

        if (!response.ok) {
            throw new Error('Network response was not ok')
        }
			
        const data = await response.json()

        if (data?.status) {
            navigateTo('/profile')
        } else {
            alert("Incorrect credentials")
        }
		
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error)
        alert('An error occurred. Please try again later.')
    }

}
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
