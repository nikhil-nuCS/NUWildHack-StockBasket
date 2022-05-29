import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './PrivateRoute.css';
import axios from 'axios'
const PrivateRoute = () => 
{
  const [email,setEmail] = useState("");
  const [password,setPassword] = useState("");

  const loginClient = (e) =>{
    e.preventDefault();
    axios.post('/login', {
      email: email,
      password: password
    })
    .then((response) => {
      window.location.href = '/home';
      console.log(response);
    }, (error) => {
      console.log(error);
    });
  }

return(
<div class="form-overlay">
<form class="login-form" method="POST" action="/login">
    <header class="login-header">
        <h2>Client log in</h2>
        <p>Login/Signup using username and password</p>
    </header>
    <div class="fields">
        <div class="field-set">
            <span class="material-icons">account_circle</span>
            <input class="form-input" aria-label="username" id="txt-input" type="text" placeholder="@Username"
                value={email} onChange={(e) =>setEmail(e.target.value)} required></input>
        </div>
        <div class="field-set">
            <span class="material-icons">key</span>
            <input class="form-input" aria-label="password" id="txt-password" type="password"
                placeholder="@Password" value={password} onChange={(e) =>setPassword(e.target.value)} required/>
        </div>
        <button class="login-btn" type="simpleQuery" onClick={(e)=>{loginClient(e)}}>Log In / Sign up</button>
    </div>
</form>
</div>

);
}
PrivateRoute.propTypes = {};

PrivateRoute.defaultProps = {};

export default PrivateRoute;
