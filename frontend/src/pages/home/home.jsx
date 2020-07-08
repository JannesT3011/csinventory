import React from "react"
import "./home.scss"
import {Link} from "react-router-dom"
import Navbar from "../../components/navbar/navbar"

class Home extends React.Component {
    state ={
        url: "/",
        warn: false,
        steamid: null
    }

    handleChange = (event) => {
        const steamid = event.target.value
        if (steamid == "" || steamid == null) {this.setState({steamid:null, url: "/"})} else { 
            const url = `/inventory/${steamid}`
            this.setState({url: url, steamid: steamid})
        }
    }

    checkState = () => {
        if (this.state.steamid == null)  {
            const element = document.getElementById("search")
            this.setState({warn: true})
            element.style.border = "1px solid red"
        }
    }

    render() {
        return (
            <div className="Home">
                <div className="welcome-text" align="center">
                    <div className="intro">
                    <h1>CS Inventory</h1>
                    <h3>The place for CS Inventorys</h3>
                    </div>
                    <form onChange={this.handleChange} className="search-form">
                        <input type="text" name="input_steamid" id="input_steamid" placeholder="Steamid..."  id="search"/>
                        {this.state.warn ? <p className="warn-msg">Please enter steamid</p> : null}
                        <Link to={this.state.url}>
                            <button onClick={this.checkState}><i className="fa fa-search"/></button>
                        </Link>
                    </form>
                </div>
            </div>
        )
    }
}

export default Home;