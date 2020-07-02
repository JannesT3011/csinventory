import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from "./pages/home/home"
import Inventory from './pages/inventory/inventory';
import InventoryStats from "./pages/inventoryStats/inventoryStats"
import InventoryHistory from "./pages/inventoryHistory/inventoryHistory"

function App() {
    return(
      <Router>
        <Route path={["/", "/home", "/index"]} exact component={Home}/>
        <Route path="/inventory/:steamid" exact component={Inventory}/>
        <Route path="/inventory/stats/:steamid" exact component={InventoryStats}/>
        <Route path="/inventory/history/:steamid" exact component={InventoryHistory}/>
      </Router>
    )
}

export default App;
