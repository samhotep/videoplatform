import React from 'react';
import logo from './logo.svg';
import './App.css';
import './w3.css';
import HomePage from './pages/homePage';

/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}*/
/*
<div className="w3-container">
      <header>
        My custom header
      </header>
      <button className="w3-btn w3-aqua">Submit</button>
    </div>s
*/

function App() {
  return (
    <HomePage />
  );
}

export default App;
