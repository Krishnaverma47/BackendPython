import { useState,useEffect } from 'react';
import axios from "axios";
import './App.css'

function App() {
  const [username, set_user_name] = useState('');
  const handle_submit = (e) =>{
    e.preventDefault();
    axios.post("http://127.0.0.1:8000/data",{   
    name:username
    })
    .then((response)=>{
      // console.log(response);
    }).catch((error)=>{
      // console.log(error);
    })
  }
  useEffect(()=>{
    axios.get("http://127.0.0.1:8000/data")
    .then((response)=>{
      console.log(response.data[0]['name']);
    })
  },[]);

  return (
    <div className="App">
      <h2>Hello react app!</h2>
      <form onSubmit={handle_submit}> 
        <input id="user_name" placeholder='Enter Your Name' value={username} onChange={(e)=>set_user_name(e.target.value)}></input>
        <input type='submit'style={{'marginTop':'10px','marginLeft':'10px' }} value="Register"/>
      </form>
    </div>
  )
}

export default App
