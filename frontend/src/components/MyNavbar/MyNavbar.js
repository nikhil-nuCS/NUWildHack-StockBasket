import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import './MyNavbar.css';
import {Link} from 'react-router-dom';
import axios from 'axios'
const MyNavbar = () => {
  const [funds,setFunds] = useState(null)
  setTimeout(()=>{
    axios.get('/userprofile/az@yop',{
      headers : {'Access-Control-Allow-Origin':'*',
    },
      crossorigin:true
    }).then(response => {
      //console.log("**SUCCdSS in get profile", response.data['az@yop'].funds)
      setFunds( response.data['az@yop'].funds)
     // console.log("fsdhgfh",funds)
    }).catch(error => {
      console.log(error)
    })
  }, 2000)
  return(
  <nav class="navbar navbar-expand-xl">
  <div class="container-fluid">
    <a class="navbar-brand text-light" href="#">StockBasket</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <Link to="/home" class="nav-link text-light" aria-current="page" href="#">Home</Link>
        </li>
        <li class="nav-item">
          <Link to='/mybasket' class="nav-link text-light" href="#">My Baskets</Link>
        </li>
        <li class="nav-item">
          <a class="nav-link text-light" href="#">WatchList</a>
        </li>
      </ul>
    </div>
    <div class="d-flex">
      <button type="button" class="btn text-light">Funds: ${funds}</button>
      <Link to="/stocks" class="btn text-light">Create Baskets</Link>
      <Link to="/login" type="button" class="btn text-light">Logout</Link>
    </div>
  </div>
</nav>
);
  }
MyNavbar.propTypes = {};

MyNavbar.defaultProps = {};

export default MyNavbar;
