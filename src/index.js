import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import SimpleExample from './App';
import Controls from './Controls';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<SimpleExample />, document.getElementById('container'))
ReactDOM.render(<Controls />, document.getElementById('controls'))

registerServiceWorker();
