import React from "react"
import "./invNavbar.scss"

class InvNavbar extends React.Component {
    render() {
        return (
            <div className="InvNavbar" align="center">
                <a href="/inventory" className="inv-nav" id="inventory-point">Inventory</a>
                <a href="/inventory/stats" className="inv-nav" id="stats-point">Inventory Stats</a>
                <a href="/inventory/history" className="inv-nav" id="history-point">Inventory History</a>
            </div>
        )
    }
}

export default InvNavbar;