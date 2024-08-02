import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  // arrow function recommended for full type inference
  const email = ref()
  const name = ref()
  const accessToken = useCookie("accessToken", {
    maxAge: 60 * 60 * 24 * 1000
  })

  const setToken = (data?: string) => (accessToken.value = data);
  const setEmail = (data?: string) => (email.value = data);
  const setName = (data?: string) => (name.value = data);

  const signIn = async (data?: any) =>{
    try{
      const response: Response = await fetch(
        'http://localhost:5001/auth/jwt/login',
        {
          method: 'POST',
          headers: {
            accept: 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded',
          },
          body: `grant_type=&username=${encodeURIComponent(
            data.email
          )}&password=${encodeURIComponent(
            data.password
          )}&scope=&client_id=&client_secret=`,
          credentials: 'include',
        }
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      //set token
		  const res_data = await response.json()
		  setToken(res_data.access_token)

      //fetch user data
      await fetchUser()
    }catch(error){
      setToken();
      setEmail();
      setName();
      console.log(error);
    }
  }

  const fetchUser = async (data?: any) =>{
    try{
      //get user fetch data
      const response = await fetch('http://localhost:5001/auth/curent_user', {
        method: 'GET',
        headers: {
            accept: 'application/json',
            Authorization: `Bearer ${accessToken.value}`,
        },
        credentials: 'include',
    })
    const res = await response.json()
    const res_parte = JSON.parse(res)

    //set state data
    if(!res_parte.detail){
      setEmail(res_parte.email)
      setName(res_parte.name)
    }
    }catch(error){
      setToken();
      setEmail();
      setName();
      console.log(error);
    }
  }

  const logout = () => {
    setToken();
    setEmail();
    setName();
  }
  
  return {email, name, accessToken, logout, signIn, fetchUser, setEmail, setName, setToken};
})