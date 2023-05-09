import './App.css'
import {React,useState} from 'react';
import axios from 'axios';

function App() {

  const [file, setFile] = useState()
  function uploadFile(event){
    event.preventDefault()
    const url = 'http://127.0.0.1:8000/uploadfile';
    const formData = new FormData();
    formData.append('file', file);
    formData.append('fileName', file.name);
    const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
    axios.post(url, formData, config).then((response) => {
      console.log(response.data);
    });

  }
  function formData(event){
    setFile(event.target.files[0])
  }
  return (
    <>
    <form className="card mt-2" method="POST" style={{'width':'18rem'}} encType="multipart/form-data" onSubmit={uploadFile}>
        <h4 className="p-2">Upload new flie</h4>
        <div className="m-3">
            <input className="form-control" type="file" id="fileupload" onChange={formData} required/>
        </div>
        <button type="submit" className="btn btn-primary m-3">Transcript</button>
    </form>
      
    </>
  )
}

export default App
