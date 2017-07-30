import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Controls from './Controls';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<Controls />, document.getElementById('controls'))

registerServiceWorker();
