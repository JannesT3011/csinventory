import React from "react"

class InvNavbar extends React.Component {
    render() {
        return (
            <div className="InvNavbar">
                <a href="/inventory"><button>Inventory</button></a>
                <a href="/inventory/stats"><button>Inventory Stats</button></a>
                <a href="/inventory/history"><button>Inventory History<button></button></button></a>
            </div>
        )
    }
}

export default InvNavbar;