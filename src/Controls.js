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
      intensity: 50
    };
  }

  handleChange = (value) => {
    this.setState({
      intensity: value
    });
  }

  render() {
    return (
      <div>
      <section className="banner style1 orient-right content-align-left image-position-center onscroll-image-fade-in" id="first">

        <div className="content">
          <h2>Magna etiam feugiat</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi id ante sed ex pharetra lacinia sit amet vel massa. Donec facilisis laoreet nulla eu bibendum. Donec ut ex risus. Fusce lorem lectus, pharetra pretium massa et, hendrerit vestibulum odio lorem ipsum dolor sit amet.</p>

          <ul className="actions vertical">
            <li><a href="#" className="button">Learn More</a></li>
            <Slider step={10} dots value={this.state.intensity} onChange={this.handleChange} />
          </ul>

          <div id='counter'>{this.state.intensity}</div>
        </div>

        <div className="image">
          <SimpleExample intensity={this.state.intensity} />
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
