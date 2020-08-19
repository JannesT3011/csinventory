import React from "react"
import "./invNavbar.scss"

class InvNavbar extends React.Component {
    render() {
        return (
            <div className="InvNavbar" align="center">
                <a href={`/inventory/${this.props.steamid}`} className="inv-nav" id="inventory-point">Inventory</a>
                <a href={`/inventory/stats/${this.props.steamid}`} className="inv-nav" id="stats-point">Inventory Stats</a>
                <a href={`/inventory/history/${this.props.steamid}`} className="inv-nav" id="history-point">Inventory History</a>
                <a href={`/inventory/share/${this.props.steamid}`} className="inv-nav" id="share-point">Share</a>
            </div>
        )
    }
}

export default InvNavbar;