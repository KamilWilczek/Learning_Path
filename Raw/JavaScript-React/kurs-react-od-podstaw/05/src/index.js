import React from 'react';
// import ReactDOM from 'react-dom';
import Root from './views/Root/Root';
import { createRoot } from 'react-dom/client';

// ReactDOM.render(<Root />, document.getElementById('root'));
const container = document.getElementById('root');
const root = createRoot(container);
root.render(<Root tab="home" />);