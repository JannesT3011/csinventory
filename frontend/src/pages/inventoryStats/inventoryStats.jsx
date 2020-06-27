import React from "react"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryStats extends React.Component {
    render() {
        return(
            <div className="inventoryStats">
                <Navbar/>
                <InvBar/>
                <h1>InventoryStats</h1>
            </div>
        )
    }
}

export default InventoryStats;