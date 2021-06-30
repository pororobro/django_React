import React,{useState} from 'react'
import './PostWrite.css'
import { Button } from '@material-ui/core';
import { userHistory } from 'react-router'
import { postWrite } from 'api';

const PostWrite = () => {
  const [postInfo, setPostInfo] = useState({
    title: '',
    content: ''
    
  })

  const {title, content} = postInfo

  
  const handleSubmit = e => {
    e.preventDefault()
    alert(`전송 클릭: ${JSON.stringify({...postInfo})}`)
    const signupRequest = {...postInfo}
    postWrite(signupRequest)
    .then(res=>{
      alert(`작성 완료: ${res.data.result}`)

    })
    .catch(err => {
      alert (`작성 실패: ${err}`)
    })
  }

  const handleClick = e => {
    e.preventDefault()
    alert('작성 취소')
  }

  const handleChange = e => {
    const { name, value } = e.target
    setPostInfo({
      ...postInfo,
      [name]: value
    })

  }


    return (<>
    <div className="PostWrite">
    <form onSubmit={handleSubmit} method="post" style={{border:"1px solid #ccc"}}>
      <div className="container">
      <h1>게시글 쓰기</h1>
        <p>Please fill in this form</p>
      
        <label for="content"><b>글내용</b></label>
        <input type="text" placeholder="글을 쓰세요" onChange={handleChange}   name="content" value={content}/>
        <label for="title"><b>글제목</b></label>
        <input type="text" placeholder="제목" onChange={handleChange}  name="title" value={title}/>

        
        <div class="clearfix">
          <button type="submit" className="writebtn">글쓰기</button>
          
        </div>
      </div>
  </form>
</div>
</>)
}

export default PostWrite