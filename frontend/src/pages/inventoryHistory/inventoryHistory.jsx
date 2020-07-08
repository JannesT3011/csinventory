import React from "react"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryHistory extends React.Component {
    state = {
        history: null,
        dates: null,
        loading: false,
        elements: null,
        selected_date: null,
        today_cashout: null,
        inv_amount: null
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
        this.setState({history: data})
        let dates = []
        let all_dates = []
        let elements = []
        Object.keys(data).map((date) => {
            all_dates.push(date)
            dates.push(
                <option value={date}>{date}</option>
            )
        })
        const _data = data[all_dates[0]]
        Object.keys(_data).map((item) => {
            if ( !(item==="inventory_amount") && !(item==="inventory_value_median") && !(item==="todays_cashout")) {
                elements.push(
                    <div className="items">
                        <h3>{item}</h3>
                        <hr/>
                        <h3>Amount: {_data[item]['amount']}</h3>
                        <h3>lowest price:{_data[item]["lowest_price"]}</h3>
                        <h3>totalcashout:{_data[item]["total_cashout"]}</h3>
                        <h3>Median Price:{_data[item]["median_price"]}</h3>
                    </div>
                )
            }
        })

        this.setState({dates: dates, elements: elements,today_cashout:_data["todays_cashout"], inv_amount: _data["inventory_amount"] ,loading: false})
        return
    }

    handleChange = (event) => {
        this.setState({selected_date: event.target.value, loading: true})
        let elements = []
        var data = this.state.history[event.target.value]
        Object.keys(data).map((item) => {
            if ( !(item==="inventory_amount") && !(item==="inventory_value_median") && !(item==="todays_cashout")) {
                elements.push(
                    <div className="items">
                        <h3>{item}</h3>
                        <hr/>
                        <h3>Amount: {data[item]['amount']}</h3>
                        <h3>lowest price:{data[item]["lowest_price"]}</h3>
                        <h3>totalcashout:{data[item]["total_cashout"]}</h3>
                        <h3>Median Price:{data[item]["median_price"]}</h3>
                    </div>
                )
            }
        })
        this.setState({elements: elements, today_cashout:data["todays_cashout"], inv_amount: data["inventory_amount"], loading: false})
        return
    }

    render() {
        return(
            <div className="inventoryHistory">
                <Navbar title="History" steamid={this.props.match.params.steamid}/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <select name="" id="" onChange={this.handleChange}>
                    {this.state.dates}
                </select>
                <br/> <br/>
                <div className="output-grid">
                    <div className="output-total" align="center">
                        Total Inventory Amount: <br/>
                        {this.state.inv_amount}
                    </div>
                    <div className="output-total" align="center">
                        Todays Cashout: <br/>
                        {this.state.today_cashout}
                    </div>
                </div>
                <br/>
                <div className="item-grid">
                    {this.state.elements}
                </div>
            </div>
        )
    } // TODO display items on selectet date -> this.state.history.date
}

export default InventoryHistory;