import React from "react"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryHistory extends React.Component {
    state = {
        history: null,
        dates: null
    }

    async componentDidMount() {
        const url = "/api/inventory/history"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": "76561198439884801"})
        })
        const data = await response.json()
        console.log(data)
        this.setState({history: data})
        let dates = []
        Object.keys(data).map((date) => {
            console.log(date)
            dates.push(
                <option value={date}>{date}</option>
            )
        })
        this.setState({dates: dates})
    }

    getInvOnDate = async() => {
        const url = "/api/inventory/history/date"
    }

    render() {
        return(
            <div className="inventoryHistory">
                <Navbar/>
                <InvBar/>
                <h1>InventoryHistory</h1>
                <form action="">
                    <select name="" id="">
                        {this.state.dates}
                    </select>
                </form>
            </div>
        )
    } // TODO display items on selectet date -> this.state.history.date
}

export default InventoryHistory;