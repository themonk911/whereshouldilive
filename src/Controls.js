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

const handle = (props) => {
  const { value, dragging, index, ...restProps } = props;
  return (
    <Tooltip
      prefixCls="rc-slider-tooltip"
      overlay={value}
      visible={dragging}
      placement="top"
      key={index}
    >
      <Handle value={value} {...restProps} />
    </Tooltip>
  );
};

class Controls extends Component {

  constructor()
  {
    super();
    this.state = {
      intensity: 1
    };
    this.increment = this.increment.bind(this);
    this.decrement = this.decrement.bind(this);
  }

  increment() {
      this.setState({
        intensity : this.state.intensity + 1
      });
  }

  decrement() {
      this.setState({
        intensity : this.state.intensity - 1
      });
  }


  //
  // handle(props) {
  //   const { value, dragging, index, ...restProps } = props;
  //     return (
  //       <Tooltip
  //         prefixCls="rc-slider-tooltip"
  //         overlay={value}
  //         visible={dragging}
  //         placement="top"
  //         key={index}
  //       >
  //         <Handle value={value} {...restProps} />
  //       </Tooltip>
  //     );
  // }


  // getColors() {
  //     return "#00FF00";
  // }

  render() {
    return (
      <div>
        <SimpleExample intensity={this.state.intensity} />

        <div id='counter'>{this.state.intensity}</div>

        <Slider min={0} max={20} defaultValue={3} handle={handle} />

        <button class="btn btn-info" onClick = {this.increment}> Add 1 </button>
        <button class="btn btn-info" onClick = {this.decrement}> Minus 1 </button>

        <ButtonToolbar>
        <Button bsStyle="primary" bsSize="large" active>Primary button</Button>
        <Button bsSize="large" active>Button</Button>
        </ButtonToolbar>
    </div>
    );
  }

}

export default Controls;
