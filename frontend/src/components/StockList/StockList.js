import React, { useState } from 'react';
import PropTypes from 'prop-types';
import './StockList.css';
import { useEffect } from 'react';
import axios from 'axios'
import { MenuItemUnstyled } from '@mui/base';

const StockList = () => {
  const [getMessage, setGetMessage] = React.useState([])
  const [userStocks, setUserStocks] = useState({
    stockList: []
  });
  useEffect(() => {
    axios.get('/tickerdata', {
      headers: { 'Access-Control-Allow-Origin': '*' },
      crossorigin: true
    }).then(response => {
      console.log("**SUCCdSS", response)
      setGetMessage(response)
      console.log("**SUCCEafdSS", getMessage.data)
    }).catch(error => {
      console.log(error)
    })

  }, [])

  const handlechange = (e) => {
    const { value, checked } = e.target;
    const { stockList } = userStocks;
    if (checked) {
      setUserStocks({
        stockList: [...stockList, value]
      })
    } else {
      setUserStocks({
        stockList: stockList.filter((e) => e !== value)
      })
    }
  }
  const getAllCheck = e => {
    var l = userStocks.stockList.length
    var q = 100 / l;
    console.log(userStocks.stockList)
    var json = userStocks.stockList.reduce((json, value, key) => { json[value] = q; return json; }, {});
    console.log(json)
    const jsonobj = {
      name:"Custom StockBasket Created",
      CAGR:"12",
      creatorId:"az@yop",
      description:"This is a custom StockBasket created by analysing the ticker data over last 4 years and predicting to choose the most finacially stable stocks.",
      imageurl:"https://picsum.photos/100",
      price:"420",
      riskType:"Medium",
      type:"Not Defined",
      stocks:json
    }
    axios.post('/usercreatedbaskets', jsonobj, {
      headers: {
        // Overwrite Axios's automatically set Content-Type
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        window.location.href = '/home'
        console.log(response);
      }, (error) => {
        console.log(error);
      });
  }
  return getMessage.data ? (
    <div class="all-stocks">
          <h3 class="stocks-section-title">Create your own customizable basket:</h3>
      <div class="all-stocks-page">
      <div class="all-stocks-section">
        {getMessage.data.slice(0, 10).map(item => (
          <div class="stock-form-check">
            <input class="form-check-input" type="checkbox" value={item.T} id="defaultCheck1" onChange={handlechange} />
            <div class="stock-form-upper">
              <img class="stock-form-logo" src={item.image_url}></img>
            </div>
            <div class="stock-form-lower">
              <label class="stock-det stock-form-code">Ticker Name: {item.T}</label>
              <label class="stock-det stock-form-name">Company Name: {item.name}</label>
              <label class="stock-det stock-form-price">Closed at: ${item.c}</label>
            </div>
          </div>
        ))}
      </div>
      <button type="simpleQuery" style={{ width: '22%', height:'45px' }} onClick={(e) => { getAllCheck(e) }} class="stock-add-btn">Add to portfolio</button>
    </div>

    </div>
  ) : null;
}

StockList.propTypes = {};

StockList.defaultProps = {};

export default StockList;
