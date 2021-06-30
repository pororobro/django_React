import React,{useState} from 'react'
import './Login.css'
import { Button } from '@material-ui/core';
import { userSignup } from 'api';
import { userLogin } from 'api';
import { userHistory } from 'react-router'

const Login = () => {
  const [userInfo, setUserInfo] = useState({
    username: '',
    password: '',
   
  })

  const {username, password} = userInfo

  const handleChange = e => {
    const { name, value } = e.target
    setUserInfo({
      ...userInfo,
      [name]: value
    })

  }

  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송 클릭: ${JSON.stringify({...userInfo})}`)
    const signupRequest = {...userInfo}
    userSignup(signupRequest)
    .then(res=>{
      alert('로그인 완료: ${res.data.result}')

    })
    .catch(err => {
      alert ('로그인 실패: ${err}')
    })
  }

  const handleClick = e => {
    e.preventDefault()
    alert('취소 클릭')
  }

    return (<>
    <div className="Signup">
    <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
      <div className="container">
        <h1>Login</h1>
      
        <hr/>

        <label for="username"><b>ID</b></label>
        <input type="text" placeholder="Enter ID" onChange={handleChange}   name="username" value={username}/>

        <label for="password"><b>Password</b></label>
        <input type="password" placeholder="Enter Password" onChange={handleChange}  name="password" value={password}/>

        
        <div class="clearfix">
          <button type="submit" className="signupbtn">login</button>
          
        </div>
      </div>
  </form>
</div>
</>)
}

export default Login