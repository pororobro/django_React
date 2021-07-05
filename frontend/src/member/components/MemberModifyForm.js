import React,{useEffect, useState} from 'react'
import 'member/styles/MemberDetail.css'
import { memberModify } from 'api'
const MemberModifyForm = () => {
    const [member, setMember] = useState({})


    useEffect(() => {
      setMember(JSON.parse(localStorage.getItem("selectedMember")))
    }, {})

    const handleSubmit = e => {
      e.preventDefault()
      alert(JSON.stringify(member))
      member.password = e.target.value
      alert(JSON.stringify(member))
      memberModify({member})
      .then(res => {
        alert(`회원가입 완료 : ${res.data.result} `)
        // history.push('login')
        
      })
      .catch(err => {
        alert(`회원가입 실패 : ${err} `)
  
      })
    }

    return (<>
             <div className="member-detail-card">
                <h2 style={{"text-align":"center"}}>상세정보 수정</h2>
                <img src="https://www.w3schools.com/w3images/team2.jpg"  style={{"width":"100%"}}/>
                <h1>{member.name}</h1>
                    <p className="member-detail-title">CEO & Founder, Example</p>
                    <p>Harvard University</p>
                    <div style={{"margin": "24px 0"}}>



                    <form method="post" onSubmit={handleSubmit} >
         

        <div className="container">
          <label labelFor="psw"><b>변경할 비밀번호</b></label>
          <input type="password" placeholder="Enter Password" name="password" required/>
              
          <button type="submit">확 인</button>
         
        </div>

      </form>





                    </div>
                    <p><button className="member-detail-button">Contact</button></p>
                </div>
                
       
      </>)
}

export default MemberModifyForm