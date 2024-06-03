import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import UserProfile from './components/UserProfile';

function App() {
    return (
        <Router>
            <div className="container">
                <Switch>
                    <Route exact path="/" component={Home} />
                    <Route path="/user/:id" component={UserProfile} />
                </Switch>
            </div>
        </Router>
    );
}

export default App;
