import React from "react"
import "./navbar.scss"

class Navbar extends React.Component { // TODO: 
    render() {
        return(
            <header className="Navbar">
                <div className="title">
                <h1>{this.props.title}</h1>
                </div>
            </header>
        )
    }
}

export default Navbar