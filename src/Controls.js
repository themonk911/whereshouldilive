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
        <SimpleExample intensity={this.state.intensity} />
        <Slider step={10} value={this.state.intensity} onChange={this.handleChange}/>
        <div id='counter'>{this.state.intensity}</div>

    </div>
    );
  }

}

export default Controls;
