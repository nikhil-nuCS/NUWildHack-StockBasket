import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './AssetManagers.css';
import {useEffect} from 'react';
import axios from 'axios'
const AssetManagers = () => {
  const [managers,setManagers] = useState([])

  useEffect(()=>{
    axios.get('/managerprofile',{
      headers : {'Access-Control-Allow-Origin':'*'},
      crossorigin:true
    }).then(response => {
      console.log("**SUCCdSS", response.data)
      setManagers(response)
      console.log("**SUCCEafdSS", managers)
    }).catch(error => {
      console.log(error)
    })

  }, [])

return managers.data?(
  <div class="asset-managers" id="asset-managers"> 
  <div class="asset-manager-title">
    <h3 class="asset-section-title">List of all the assets managers:</h3>
  </div>
  <div class="asset-basket-wrapper">
    {managers.data.map(item => (
      <div href="#" class="list-group-item list-group-item-action all-basket-item">
      <div class="image-basket-container">
        <img src={item.imageurl} class="img-thumbnail asset-manager-image" alt="..." />
        <div class="basket-content">
          <div class="d-flex w-100 justify-content-between">
            <h5 class="mb-1 basket-title">{item.name}</h5>
          </div>
          <p class="mb-1 basket-text">{item.description}</p>
          <div style={{ textAlign: 'left', color: '#808080' }}>Rating: {item.ratings}</div>
        </div>
      </div>
    </div>

    ))}
  </div>
</div>
):null;
}
AssetManagers.propTypes = {};

AssetManagers.defaultProps = {};

export default AssetManagers;
