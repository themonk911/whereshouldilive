import React, { Component }  from 'react'
import { render } from 'react-dom'

class Controls extends Component {

  constructor()
  {
    super();
    this.state = {
      intensity: 1
    };
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

  render() {
    return (
      <div>
        <div id='counter'>{this.state.intensity}</div>
        <button onClick = {this.increment}> Add 1 </button>
        <button onClick = {this.decrement}> Minus 1 </button>
    </div>
    );
  }

}

export default Controls;
