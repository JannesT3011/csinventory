import React from "react"
import "./navbar.scss"

class Navbar extends React.Component { // TODO: 
    render() {
        return(
            <div className="Navbar">
                <a href="/"><img src="" alt="LOGO"/></a>
                <a href="/inventory">Inventory</a>
                <a href="/stats">stats</a>
                <a href="/login" className="steamlogin-img"><img src="https://steamcommunity-a.akamaihd.net/public/images/signinthroughsteam/sits_01.png" alt="steamlogin"/></a>
            </div>
        )
    }
}

export default Navbar