
<template>
  <Nav/>
  <Signup/>
</template>

<script>
  import Signup from '../components/Signup.vue'
  import Nav from '../components/Nav.vue'

  export default{
    name: 'SignupView',
    components:{
      Nav,
      Signup
    }
  }
  
</script>
