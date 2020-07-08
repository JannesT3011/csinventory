import React from "react"
import "./navbar.scss"
import {Link, Redirect} from "react-router-dom"

class Navbar extends React.Component {
    state = {
        url: "/",
        warn: false,
        steamid: null, 
        redirect: false
    }

    handleChange = (event) => {
        const steamid = event.target.value
        if (steamid == "" || steamid == null) {this.setState({url: `/`, steamid:null})} else {
            const url = `/inventory/${steamid}`
            this.setState({url: url, steamid: steamid})
        }
    }

    checkState = () => {
        if (this.state.steamid == null) {
            // this.setState({url: `/inventory/${this.props.match.params.steamid}`})
            const element = document.getElementById("newsteamid-input")
            element.style.border = "1px solid red"
        }
    }

    render() {
        return(
            <div className="topnav">
                <a href="/" className="active" className="to-home">Home</a>
                <div className="search-container">
                    <form onChange={this.handleChange} action={this.state.url}>
                        <input type="text" placeholder="SteamID.." id="newsteamid-input"/>
                        <button type="submit" onClick={this.checkState}><i className="fa fa-search"></i></button>           
                    </form>
                </div>
            </div>
        )
    }   
}

export default Navbar