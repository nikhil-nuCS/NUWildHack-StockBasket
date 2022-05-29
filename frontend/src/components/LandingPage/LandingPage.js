import React from 'react';
import PropTypes from 'prop-types';
import './LandingPage.css';
import { Link } from 'react-router-dom';
const LandingPage = () => (
  <div class="landing-page">
    <h2 class="landing-title">StockBasket</h2>
    <h4 class="landing-subtitle">There's an investment for everyone</h4>

    <img class="landing-logo" src="https://cdn-icons-png.flaticon.com/512/6978/6978350.png"></img>
    <div class="landing-content">
      <div class="card text-center option-card">
        <div class="card-header">
          Client Login
        </div>
        <div class="card-body">
          <p class="card-text">Welcome, Login as a Client</p>
          <Link to="/login" href="#" class="btn btn-primary landing-button">Client Login</Link>
        </div>
      </div>
      <div class="card text-center option-card">
        <div class="card-header">
          Vendor Login
        </div>
        <div class="card-body">
          <p class="card-text">Welcome, Login as a Vendor</p>
          <Link to="/vlogin" href="#" class="btn btn-primary landing-button">Vendor Login</Link>
        </div>
      </div>
    </div>
    <div class="landing-content-footer">
        <label>Nikhil Khandelwal</label>
        <label>Akshay Gupta</label>
        <label>Ritwik Kumar Singh</label>
      </div>

  </div>
);

LandingPage.propTypes = {};

LandingPage.defaultProps = {};

export default LandingPage;
