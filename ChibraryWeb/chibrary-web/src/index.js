import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom'
import { ThemeProvider } from '@material-ui/core/styles';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import MainPage from './pages/mainPage.js'
import Search from './pages/search'
import Config from "./config.ts"
import utils from "./utils"

console.disableYellowBox = true

utils.showTimeInit()

ReactDOM.render(
  <ThemeProvider theme={Config.theme}>
    <Router>
      <Route path="/index" component={MainPage} />
      <Route path="/search" component={Search} />
      <Redirect from="/" to="/index" />
    </Router>
  </ThemeProvider>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
