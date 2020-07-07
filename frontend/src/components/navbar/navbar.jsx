import React from "react"
import "./navbar.scss"
import {Link} from "react-router-dom"

class Navbar extends React.Component {
    state = {
        url: "/",
        warn: false,
        steamid: null
    }

    handleChange = (event) => {
        const steamid = event.target.value
        const url = `/inventory/${steamid}`
        this.setState({steamid: steamid, url: url})
    }

    render() {
        return(
            <div className="topnav">
                <a href="/" className="active" className="to-home">Home</a>
                <div className="search-container">
                    <form onChange={this.handleChange}>
                        <input type="text" placeholder="SteamID.."/>
                        <Link to={this.state.url}>
                            <button type="submit"><i className="fa fa-search"></i></button>
                        </Link>
                    </form>
                </div>
            </div>
        )
    }   
}

export default Navbar