// frontend/src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import JokeList from './pages/JokeList';
import JokeAnalytics from './pages/JokeAnalytics';
import './styles/global.css';

function App() {
  return (
    <Router>
      <div>
        {/* Add your header here */}
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/jokes" component={JokeList} />
          <Route path="/analytics" component={JokeAnalytics} />
          {/* Add more routes as needed */}
        </Switch>
        {/* Add your footer here */}
      </div>
    </Router>
  );
}

export default App;
