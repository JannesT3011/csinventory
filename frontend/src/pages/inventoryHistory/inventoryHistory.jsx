import React from "react"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryHistory extends React.Component {
    state = {
        history: null,
        dates: null,
        loading: false
    }

    async componentDidMount() {
        this.setState({loading: true})
        var element = document.getElementById("history-point")
        element.style.backgroundColor = "#fff"
        element.style.color = "#353535"
        const url = "/api/inventory/history"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": this.props.match.params.steamid})
        })
        const data = await response.json()
        console.log(data)
        this.setState({history: data})
        let dates = []
        Object.keys(data).map((date) => {
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
                <Navbar title="History"/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <h1>InventoryHistory</h1>
                <form action="">
                    <select name="" id="">
                        {this.state.dates}
                    </select>
                </form>
                <div className="item-grid">
                </div>
                <h1>{this.props.match.params.steamid}</h1>
            </div>
        )
    } // TODO display items on selectet date -> this.state.history.date
}

export default InventoryHistory;