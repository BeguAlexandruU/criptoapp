export default defineEventHandler(async event => {
    try {
        const accessToken = getCookie(event, 'accessToken')
        const fetch_res = await fetch('http://localhost:5001/auth/curent_user', {
            method: 'GET',
            headers: {
                accept: 'application/json',
                Authorization: `Bearer ${accessToken}`,
            },
            credentials: 'include',
        })
        const res = await fetch_res.json()
        if(res.detail){
            return { status: false }
        }

        return { status: true, data: res }
    }catch (error) {
        return { status: false }
    }
})
