import React from 'react'
import { useState, useEffect } from 'react';
import axios from "axios";
function Register() {


    const [user_name, set_user_name] = useState('');
    const [email_id, set_email_id] = useState('');
    const [password, set_password] = useState('');
    const handle_submit = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/createUser", {
            name : user_name,
            email : email_id,
            password:password
        })
            .then((response) => {
                alert(response.data['message']);
            }).catch((error) => {
                console.log(error);
            })
    }
    // useEffect(() => {
    //     axios.get("http://127.0.0.1:8000/data")
    //         .then((response) => {
    //             console.log(response.data[0]['name']);
    //         })
    // }, []);



    return (
        <div className='container main-container'>
            <div className="card"style={{ 'width': '18rem' }}>
                <div className="card-header text-center">
                    Registration
                </div>
                <div className="card-body">
                    <form method ="POST" onSubmit={handle_submit}>
                        <div className="mb-3">
                            <label htmlFor="username" className="form-label">Username</label>
                            <input type="text" value={user_name} className="form-control" id="username" onChange={(e)=>set_user_name(e.target.value)} />
                        </div>

                        <div className="mb-3">
                            <label htmlFor="emailaddress" className="form-label">Email address</label>
                            <input type="email" value={email_id} className="form-control" id="emailaddress"  onChange={(e)=>set_email_id(e.target.value)}/>
                        </div>

                        <div className="mb-3">
                            <label htmlFor="Password" className="form-label">Password</label>
                            <input type="password" value={password} className="form-control" id="Password" onChange={(e)=>set_password(e.target.value)} />
                        </div>

                        <button type="submit" className="btn btn-success">Register</button>
                    </form>
                </div>

            </div>
        </div>
    )
}

export default Register
