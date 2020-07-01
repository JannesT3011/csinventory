import React from "react"
import "./invNavbar.scss"

class InvNavbar extends React.Component {
    render() {
        return (
            <div className="InvNavbar" align="center">
                <a href="/inventory" className="inv-nav">Inventory</a>
                <a href="/inventory/stats" className="inv-nav">Inventory Stats</a>
                <a href="/inventory/history" className="inv-nav">Inventory History</a>
            </div>
        )
    }
}

export default InvNavbar;