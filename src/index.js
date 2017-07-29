import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import SimpleExample from './App';
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(<SimpleExample />, document.getElementById('container'))
registerServiceWorker();
