import React from 'react';
import PropTypes from 'prop-types';
import styles from './Footer.module.css';

const Footer = () => (
  <footer class="bg-light text-center text-lg-start fixed-bottom">
  <div class="container p-4">
    <div class="row" style={{height:'15%'}}>
      <div class="col">
        <h5 class="card-title">About</h5>

        <p class="card-text">
          StockBasket Build platforms and investment products to invest better in equites. A basket of stock/ETFS curated to reflect an idea.
        </p>
      </div>
      <div class="col">
        <h5 class="card-title">Disclaimer</h5>
        <p class="card-text">
        Investing in Stocks/ETFS are subject to market risk. Read all the related documents before investing.
        </p>
      </div>
    </div>
  </div>
</footer>
);

Footer.propTypes = {};

Footer.defaultProps = {};

export default Footer;
