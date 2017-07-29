import React, { Component }  from 'react'
import { render } from 'react-dom'
import SimpleExample from './App'

import 'rc-slider/assets/index.css';
import 'rc-tooltip/assets/bootstrap.css';

import Tooltip from 'rc-tooltip';
import Slider from 'rc-slider';

const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);

const Handle = Slider.Handle;

class Controls extends Component {

  constructor()
  {
    super();
    this.state = {
      intensity1: 10,
      intensity2: 20,
      intensity3: 30,
      intensity4: 40,
      intensity5: 50,
      intensity6: 60
    };
  }

  handleChange1 = (value) => {
    this.setState({
      intensity1: value
    });
  }
  handleChange2 = (value) => {
    this.setState({
      intensity2: value
    });
  }

  handleChange3 = (value) => {
    this.setState({
      intensity3: value
    });
  }
  handleChange4 = (value) => {
    this.setState({
      intensity4: value
    });
  }
  handleChange5 = (value) => {
    this.setState({
      intensity5: value
    });
  }
  handleChange6 = (value) => {
    this.setState({
      intensity6: value
    });
  }

  render() {
    return (
      <div>
      <section className="banner style1 orient-right content-align-left image-position-center onscroll-image-fade-in" id="second">

        <div className="content">
          <h2>Magna etiam feugiat</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id ante sed ex pharetra lacinia sit amet vel massa. Donec facilisis laoreet nulla eu bibendum. Donec ut ex risus. Fusce lorem lectus, pharetra pretium massa et, hendrerit vestibulum odio lorem ipsum dolor sit amet.</p>

          <ul className="actions vertical">
            <li>
              Police Stations
              <Slider step={10} dots value={this.state.intensity1} onChange={this.handleChange1} />
            </li>
            <li>
              Parks
              <Slider step={10} dots value={this.state.intensity2} onChange={this.handleChange2} />
            </li>
            <li>
              Traffic
              <Slider step={10} dots value={this.state.intensity3} onChange={this.handleChange3} />
            </li>
            <li>
              Food
              <Slider step={10} dots value={this.state.intensity4} onChange={this.handleChange4} />
            </li>
            <li>
              Food
              <Slider step={10} dots value={this.state.intensity5} onChange={this.handleChange5} />
            </li>
            <li>
              Food
              <Slider step={10} dots value={this.state.intensity6} onChange={this.handleChange6} />
            </li>
          </ul>

          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id ante sed ex pharetra lacinia sit amet vel massa. Donec facilisis laoreet nulla eu bibendum. Donec ut ex risus. Fusce lorem lectus, pharetra pretium massa et, hendrerit vestibulum odio lorem ipsum dolor sit amet.</p>

          <ul className="actions vertical">
            <li><a href="#third" className="button smooth-scroll-middle">Learn More</a></li>
          </ul>

        </div>

        <div className="image" alt="">
            <SimpleExample
            intensity1={this.state.intensity1}
            intensity2={this.state.intensity2}
            intensity3={this.state.intensity3}
            intensity4={this.state.intensity4}
            intensity5={this.state.intensity5}
            intensity6={this.state.intensity6}
           />
        </div>
        </section>

</div>

        // <SimpleExample intensity={this.state.intensity} />
        // <Slider step={10} dots value={this.state.intensity} onChange={this.handleChange}/>
        // <div id='counter'>{this.state.intensity}</div>

    );
  }

}

export default Controls;
