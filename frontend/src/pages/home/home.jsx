import React from "react"
import "./home.scss"
import {Link} from "react-router-dom"
import Navbar from "../../components/navbar/navbar"

class Home extends React.Component {
    state ={
        url: "/"
    }

    handleSubmit = (event) => {
        const steamid = event.target.value
        const url = `/inventory/${steamid}`
        this.setState({url: url})
    }
    render() {
        return (
            <div className="Home">
                <div className="welcome-text" align="center">
                    <h1>CS Invest</h1>
                    <h3>The place for your CS Investments</h3>
                    <form onChange={this.handleSubmit}>
                        <input type="text" name="input_steamid" id="input_steamid" placeholder="Steamid..."/>
                    </form>
                    <Link to={this.state.url}>
                        <button>Search!</button>
                    </Link>
                </div>
            </div>
        )
    }
}

export default Home;