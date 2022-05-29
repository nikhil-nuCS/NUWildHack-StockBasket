import logo from './logo.svg';
import './App.css';
import React, { Component }  from 'react';
import Button from '@mui/material/Button';
import 'bootstrap/dist/css/bootstrap.min.css';
import MyNavbar from './components/MyNavbar/MyNavbar';
import DashboardMenu from './components/DashboardMenu/DashboardMenu';
import ExploreAll from './components/ExploreAll/ExploreAll';
import {BrowserRouter as Router,Route, Switch} from 'react-router-dom';
import StockList from './components/StockList/StockList';
import PrivateRoute from './components/PrivateRoute/PrivateRoute';
import LandingPage from './components/LandingPage/LandingPage';
import MyBasketPage from './components/MyBasketPage/MyBasketPage';
import PrivateRouteVendor from './components/PrivateRouteVendor/PrivateRouteVendor';
import Footer from './components/Footer/Footer';

function App() {
  return (
    <Router>
    <div className="App">
    <Switch>
      <Route extact path ='/home' >
      <MyNavbar></MyNavbar>
      <DashboardMenu/>
      </Route>
  <Route extact path ='/stocks'>
  <MyNavbar></MyNavbar>
    <StockList></StockList>
  </Route>
  <Route extact path ='/login' >
      <PrivateRoute/>
  </Route>
  <Route extact path ='/vlogin' >
    <PrivateRouteVendor></PrivateRouteVendor>
  </Route>

  <Route extact path ='/mybasket'>
  <MyNavbar></MyNavbar>
    <MyBasketPage></MyBasketPage>
  </Route>
  <Route extact path ='/'>
    <LandingPage></LandingPage>
  </Route>
  </Switch>
    </div>
  </Router>
  );
}

export default App;
