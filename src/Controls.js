import React, { Component }  from 'react'
import { render } from 'react-dom'
import DataConnector from './App'

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
      education_intensity: 50,
      safety_intensity: 80,
      nature_intensity: 50,
      health_intensity: 80,
      housing_intensity: 10,
      transport_intensity: 50
    };
  }

  handleChange1 = (value) => {
    this.setState({
      education_intensity: value
    });
  }
  handleChange2 = (value) => {
    this.setState({
      safety_intensity: value
    });
  }

  handleChange3 = (value) => {
    this.setState({
      nature_intensity: value
    });
  }
  handleChange4 = (value) => {
    this.setState({
      health_intensity: value
    });
  }
  handleChange5 = (value) => {
    this.setState({
      housing_intensity: value
    });
  }
  handleChange6 = (value) => {
    this.setState({
      transport_intensity: value
    });
  }

  render() {
    return (
      <div>
      <section className="banner style1 orient-right content-align-left image-position-center onscroll-image-fade-in" id="first">

        <div className="content">
          <h2>Choose what matters to you</h2>
          <p>
          Each of the sliders corresponds to a factor which influences where you might want to live. Drag the sliders to indicate the importance of each one to your needs, and watch the heatmap change in response.
          </p>

          <ul className="actions vertical">
            <li>
              Education
              <Slider step={10} dots value={this.state.education_intensity} onChange={this.handleChange1} />
            </li>
            <li>
              Safety
              <Slider step={10} dots value={this.state.safety_intensity} onChange={this.handleChange2} />
            </li>
            <li>
              Nature
              <Slider step={10} dots value={this.state.nature_intensity} onChange={this.handleChange3} />
            </li>
            <li>
              Health
              <Slider step={10} dots value={this.state.health_intensity} onChange={this.handleChange4} />
            </li>
            <li>
              Housing
              <Slider step={10} dots value={this.state.housing_intensity} onChange={this.handleChange5} />
            </li>
            <li>
              Transport
              <Slider step={10} dots value={this.state.transport_intensity} onChange={this.handleChange6} />
            </li>
          </ul>          

          <ul className="actions vertical">
            <li><a href="#second" className="button smooth-scroll-middle"> Find out how it works </a></li>
          </ul>

        </div>

        <div className="image" alt="">
            <DataConnector
            education_intensity={this.state.education_intensity}
            safety_intensity={this.state.safety_intensity}
            nature_intensity={this.state.nature_intensity}
            health_intensity={this.state.health_intensity}
            housing_intensity={this.state.housing_intensity}
            transport_intensity={this.state.transport_intensity}
           />
        </div>
        </section>

</div>

        // <DataConnector intensity={this.state.intensity} />
        // <Slider step={10} dots value={this.state.intensity} onChange={this.handleChange}/>
        // <div id='counter'>{this.state.intensity}</div>

    );
  }

}

export default Controls;
