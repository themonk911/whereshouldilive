import React, { Component }  from 'react'
import { render } from 'react-dom'
import SimpleExample from './App'

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

  render() {
    return (
      <div>
        <SimpleExample intensity={this.state.intensity} />
        <div id='counter'>{this.state.intensity}</div>
        <button onClick = {this.increment}> Add 1 </button>
        <button onClick = {this.decrement}> Minus 1 </button>
    </div>
    );
  }

}

export default Controls;
