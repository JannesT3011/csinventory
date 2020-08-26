import React from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';
// ROUTES
import Home from "./pages/home/home"
import Inventory from './pages/inventory/inventory';
import InventoryStats from "./pages/inventoryStats/inventoryStats"
import InventoryHistory from "./pages/inventoryHistory/inventoryHistory"
import InventoryShare from "./pages/inventoryShare/inventoryShare"
import NotFound from './pages/notFound/notFound';

function App() {
    return(
      <Router>
        <Switch>
          <Route path={["/", "/home", "/index"]} exact component={Home}/>
          <Route path="/inventory/:steamid" exact component={Inventory}/>
          <Route path="/inventory/stats/:steamid" exact component={InventoryStats}/>
          <Route path="/inventory/history/:steamid" exact component={InventoryHistory}/>
          <Route path="/inventory/share/:steamid" exact component={InventoryShare}/>
          <Route path="*" exact component={NotFound}/>
        </Switch>
      </Router>
    )
}

export default App;
