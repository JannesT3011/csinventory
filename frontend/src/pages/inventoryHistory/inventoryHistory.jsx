import React from "react"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryHistory extends React.Component {
    state = {
        history: null
    }

    async componentDidMount() {
        const url = "api/inventory/history"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": ""})
        })
        const data = await response.json()
        this.setState({history: data})
    }

    render() {
        return(
            <div className="inventoryHistory">
                <Navbar/>
                <InvBar/>
                <h1>InventoryHistory</h1>
            </div>
        )
    }
}

export default InventoryHistory;