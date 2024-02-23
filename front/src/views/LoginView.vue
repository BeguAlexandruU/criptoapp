
<template>
  <Nav/>
  <Login/>
</template>

<script>
  import Login from '../components/Login.vue'
  import Nav   from '../components/Nav.vue'

  export default{
    name: 'LoginView',
    components:{
      Nav,
      Login
    }
  }
  
</script>
