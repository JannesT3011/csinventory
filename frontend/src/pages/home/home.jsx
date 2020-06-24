import React from "react"
import "./home.scss"
import Navbar from "../../components/navbar/navbar"

class Home extends React.Component {
    render() {
        return (
            <div className="Home">
                <Navbar/> 
                <div className="welcome-text" align="center">
                    <h1>CS Invest</h1>
                    <h3>The place for your CS Investments</h3>
                    <a href="/inventory"><button>Start!</button></a>
                </div>
            </div>
        )
    }
}

export default Home;