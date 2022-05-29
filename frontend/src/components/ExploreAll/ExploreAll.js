import React from 'react';
import PropTypes from 'prop-types';
import './ExploreAll.css';

const ExploreAll = ({setShowExplore}) => {
  const showExplore = ()=>{
    setShowExplore(3)
  }
return(
  <div class="explore" id="explore">
  <div class="container">
    <div class="row row-cols-2">
      <div class="col">
        <div class="card">
          <div class="card-header">
            Featured
          </div>
          <div class="card-body">
            <h5 class="card-title">Find your next Basket</h5>
            <p class="card-text">Move forward in your investment journey</p>
            <a href="#" class="btn btn-primary card-btn">See Next Steps</a>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-header">
            Featured
          </div>
          <div class="card-body">
            <h5 class="card-title">Brains Behind Baskets</h5>
            <p class="card-text">Baskets are managed by top-registered asset managers and firms.</p>
            <a href="#" class="btn btn-primary card-btn" onClick={showExplore}>See all managers</a>
          </div>
        </div>
      </div>
    </div>
    <hr />
    <div class="row row-cols-4">
    <div class="col">
      <div class="card-wrapper">
          <div class="card" style={{width: '18rem'}}>
            <img src="https://www.smallcase.com/static/svgs/horizon/Target-Year-Optimisation.svg" class="card-img-top card-img-size" alt="..."/>
            <div class="card-body">
            <p class="card-text">Horizon Basket</p>
            <footer class="blockquote-footer"> Fin.Inc</footer>
            <p class="card-text">Investement done according to your goals and your dreams with a target in mind</p>
            </div>
          </div>
        </div>
    </div>
    <div class="col">
      <div class="card-wrapper">
          <div class="card" style={{width: '18rem'}}>
            <img src="https://assets.smallcase.com/images/collections/200/8Hn4KgdWWx9v79Ri8WawM.png" class="card-img-top card-img-size" alt="..."/>
            <div class="card-body">
            <p class="card-text">ETFs</p>
            <footer class="blockquote-footer"> Capital.inc</footer>
            <p class="card-text">Model portfolio built using exchange traded funds</p>
            </div>
          </div>
        </div>
    </div>
    <div class="col">
      <div class="card-wrapper">
          <div class="card" style={{width: '18rem'}}>
            <img src="https://assets.smallcase.com/images/collections/200/ik9-A3LaD.png" class="card-img-top card-img-size" alt="..."/>
            <div class="card-body">
            <p class="card-text">Popular Investment Ideas</p>
            <footer class="blockquote-footer"> mill.inc</footer>
            <p class="card-text">Based on ideas that are trending among investors.</p>
            </div>
          </div>
        </div>
    </div>
    <div class="col">
      <div class="card-wrapper">
          <div class="card" style={{width: '18rem'}}>
            <img src="https://assets.smallcase.com/images/collections/200/GKPw4-QVb.png" class="card-img-top card-img-size" alt="..."/>
            <div class="card-body">
            <p class="card-text">New Investors strategy</p>
            <footer class="blockquote-footer">Ethical Advisers</footer>
            <p class="card-text">For new investors to start their wealth creation journey</p>
            </div>
          </div>
        </div>
    </div>
    
    </div>
    <hr/>
    <div class="row row-cols-2">
      <div class="col">
        <div class="card">
        <div class="card-header">About</div>
          <div class="card-body">
            
            <p class="card-text"> StockBasket Builds platforms and investment products to invest better in equites. A basket of stock/ETFS curated to reflect an idea.</p>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
        <div class="card-header">Disclaimer</div>
          <div class="card-body">
            
            <p class="card-text">Investing in Stocks/ETFS are subject to market risk. Read all the related documents before investing.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  
</div>
);
}
ExploreAll.propTypes = {};

ExploreAll.defaultProps = {};

export default ExploreAll;
