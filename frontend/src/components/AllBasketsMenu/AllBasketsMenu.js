import React from 'react';
import PropTypes from 'prop-types';
import './AllBasketsMenu.css';
import { Button } from 'react-bootstrap';
import { Modal } from 'react-bootstrap';
import { useState } from 'react';
import { useEffect } from 'react';
import axios from 'axios'
const AllBasketsMenu = () => {
  const [show, setShow] = useState(false);
  const [item, setItem] = useState(-1)
  const [baskets, setBaskets] = useState([]);
  useEffect(() => {
    axios.get('/baskets', {
      headers: { 'Access-Control-Allow-Origin': '*' },
      crossorigin: true
    }).then(response => {
      console.log("**SUCCdSS", response.data)
      setBaskets(response)
      console.log("**SUCCEafdSS", baskets)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  const handleClose = (item) => {
    setShow(false);
  }
  const handleShow = (e) => {
    setShow(true);
    console.log(e.currentTarget.getAttribute('index'))
    setItem(e.currentTarget.getAttribute('index'))
  }
  const setCheck = e => {

  }
  const handlesubmit = (e) => {
    const json = {
      email: 'az@yop',
      basketid: baskets.data[item].id,
      quantity: '1'
    }
    console.log(json)
    axios.post('/investedbaskets', json, {
      headers: {
        // Overwrite Axios's automatically set Content-Type
        'Content-Type': 'application/json'
      }
    })
      .then((response) => {
        console.log(response);
        setShow(false);
      }, (error) => {
        console.log(error);
      });
  }
  return baskets.data ? (
    <div class="basket-content">
      <h3 class="section-title-allbasket"> List of available baskets:</h3>
      <label class="section-text-allbasket"> Choose any basket and add it to your portfolio.</label>
      <div class="all-baskets" id="all-baskets">
        {baskets.data[item] ? (<Modal show={show} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>{baskets.data[item].name}</Modal.Title>
          </Modal.Header>
          <Modal.Body>{baskets.data[item].description}</Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Close
            </Button>
            <Button style={{backgroundColor:"#326E90"}} onClick={(e) => { handlesubmit(e) }}>
              Buy This Basket
            </Button>
          </Modal.Footer>
        </Modal>) : null
        }
        <div class="basket-wrapper">
          <div class="list-group all-basket-list">
            {baskets.data.map((item, index) => (
              <div href="#" index={index} class="list-group-item list-group-item-action all-basket-item" onClick={(e) => handleShow(e)}>
                <div class="image-basket-container">
                  <img src={item.imageurl} class="img-thumbnail" alt="..." />
                  <div class="basket-content">
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1 basket-title">{item.name}</h5>
                    </div>
                    <p class="mb-1 basket-text">{item.description}</p>
                    <div style={{ textAlign: 'left' }}>Price: ${item.price}</div>
                    <div style={{ textAlign: 'left', color: '#808080' }}>Risk Type: {item.riskType}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  ) : null;
}
AllBasketsMenu.propTypes = {};

AllBasketsMenu.defaultProps = {};

export default AllBasketsMenu;
