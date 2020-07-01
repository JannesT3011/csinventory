import React from "react"
import "./navbar.scss"

class Navbar extends React.Component { // TODO: 
    render() {
        return(
            <div className="Navbar">
                <a href="/"><img src="" alt="LOGO"/></a>
                <a href="/inventory">Inventory</a>
                <a href="/stats">stats</a>
            </div>
        )
    }
}

export default Navbar