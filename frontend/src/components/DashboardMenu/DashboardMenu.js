import React from 'react';
import PropTypes from 'prop-types';
import './DashboardMenu.css';
import ExploreAll from '../ExploreAll/ExploreAll';
import AllBasketsMenu from '../AllBasketsMenu/AllBasketsMenu';
import { findRenderedComponentWithType } from 'react-dom/test-utils';
import AssetManagers from '../AssetManagers/AssetManagers';
const showbasket = () =>{
  


}
// const showall = (e) =>{
// console.log("*",e.target)
// if(e.id == 2){
//   setShowExplore(2)
// }
// }
const showassets = () =>{


}
const DashboardMenu = () => {
const [showExplore,setShowExplore] = React.useState(1)
const showall = (e) =>{
 // console.log("*dff",e.target)
  
    console.log("*dff",e.target)
    setShowExplore(e.target.id)
  
  }
return (
  <div class="menu-dashboard">
  <ul class="nav nav-pills">
      <li class="nav-item">
        <a class="nav-link text-dark" id="1" aria-current="page" href="#" onClick={e => showall(e)} data-value="explore" >Explore</a>
      </li>

      <li class="nav-item">
        <a class="nav-link text-dark" id="2" href="#" onClick={e => showall(e)} data-value="all-baskets">All Baskets</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-dark" id ="3" href="#" onClick={e => showall(e)} data-value="asset-managers">Asset Managers</a>
      </li>
    </ul>
    { showExplore == 1 ? <ExploreAll setShowExplore={setShowExplore}></ExploreAll> : showExplore == 2 ? <AllBasketsMenu></AllBasketsMenu> : showExplore ==3 ? <AssetManagers></AssetManagers>:null
      
    }
   

</div>
);
}
DashboardMenu.propTypes = {};

DashboardMenu.defaultProps = {};

export default DashboardMenu;
