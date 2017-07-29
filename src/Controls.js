import React, { Component }  from 'react'
import { render } from 'react-dom'
import SimpleExample from './App'

import { Button, ButtonToolbar } from 'react-bootstrap';

import 'rc-slider/assets/index.css';
import 'rc-tooltip/assets/bootstrap.css';

import Tooltip from 'rc-tooltip';
import Slider from 'rc-slider';

const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);

const Handle = Slider.Handle;

// const handleSlider = (props) => {
//   const { value, dragging, index, ...restProps } = props;
//   return (
//     <Tooltip
//       prefixCls="rc-slider-tooltip"
//       overlay={value}
//       visible={dragging}
//       placement="top"
//       key={index}
//     >
//       <Handle value={value} {...restProps} />
//     </Tooltip>
//   );
// };

class Controls extends Component {

  constructor()
  {
    super();
    this.state = {
      intensity: 1
    };
    // this.increment = this.increment.bind(this);
    // this.decrement = this.decrement.bind(this);
    // this.handleSlider = this.handleSlider.bind(this);
  }

  // increment() {
  //     this.setState({
  //       intensity : this.state.intensity + 1
  //     });
  // }
  //
  // decrement() {
  //     this.setState({
  //       intensity : this.state.intensity - 1
  //     });
  // }



  // handleSlider(props) {
  //   //const { value, dragging, index, ...restProps } = props;
  //     this.setState({
  //       intensity: props.value
  //     });
  //     console.log(props.value);
  //     return (
  //       <Tooltip
  //         prefixCls="rc-slider-tooltip"
  //         overlay={props.value}
  //         visible={props.dragging}
  //         placement="top"
  //         key={props.index}
  //       >
  //         <Handle value={props.value} {...props.restProps} />
  //       </Tooltip>
  //     );
  // }


  // getColors() {
  //     return "#00FF00";
  // }
//        <Slider min={0} max={20} defaultValue={3} handle={this.handleSlider} />

  handleChange = (value) => {
    this.setState({
      intensity: value
    });
  }


  render() {
    return (
      <div>
        <SimpleExample intensity={this.state.intensity} />
        <Range value={this.state.value} onChange={this.handleChange}/>
        <div id='counter'>{this.state.intensity}</div>

        <ButtonToolbar>
        <Button bsStyle="primary" bsSize="large" active>Primary button</Button>
        <Button bsSize="large" active>Button</Button>
        </ButtonToolbar>
    </div>
    );
  }

}

export default Controls;
