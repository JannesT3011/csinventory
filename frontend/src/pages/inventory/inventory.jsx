import React from "react"
import Navbar from "../../components/navbar/navbar"
import "./inventory.scss"
import InvBar from "../../components/invNavBar/invNavbar"
import Loading from "../../components/loading/loading"

class Inventory extends React.Component { // TODO QR -COde for current url
    state = {
        items: null,
        elements:null,
        today_cashout: null,
        inv_amount: null,
        loading: false,
        last_refresh: null
    }

    updateInventory = async() => {
        this.setState({loading: true})
        const url = "/api/inventory/refresh/" + this.props.match.params.steamid
        const response = await fetch(url)
        this.setState({loading: false})
        window.location.reload()
    }

    async componentDidMount() { 
        this.setState({loading: true})
        var element = document.getElementById("inventory-point")
        element.style.backgroundColor = "#fff"
        element.style.color = "#353535"
        const url = "/api/inventory"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": this.props.match.params.steamid, "update": false, "api_key": ""})
        })
        const data = await response.json()
        this.setState({items: data, last_refresh: data["last_refresh"]})
        let elements = []

        Object.keys(data).map((item) => {
            if ( !(item==="inventory_amount") && !(item==="inventory_value_median") && !(item==="todays_cashout")) {
                elements.push(
                    <div className="items">
                        <h3>{item}</h3>
                        <hr/>
                        <h3>Amount: {data[item]["amount"]}</h3>
                        <h3>Lowest Price:{data[item]["lowest_price"]}</h3>
                        <h3>Total Cashout:{data[item]["total_cashout"]}</h3>
                        <h3>Median Price:{data[item]["median_price"]}</h3>
                    </div>
                )
            }
        })

        this.setState({elements:elements, today_cashout:data["todays_cashout"], inv_amount: data["inventory_amount"], loading: false})
        setInterval(response, 5000)
    }
    
    render() { 
        return (
            <section className="Inventory">
                <Navbar title="Inventory" steamid={this.props.match.params.steamid}/>
                <br/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <br/>
                <div className="updater" align="center">
                    {this.state.loading ? <Loading/> : <button onClick={this.updateInventory} className="update">Update!</button>} <br/> <br/>
                </div>
                <div className="output-grid">
                    <div className="output-total" align="center">
                        Total Inventory Amount: <br/>
                        {this.state.inv_amount}
                    </div>
                    <div className="output-total" align="center">
                        Todays Cashout: <br/>
                        {this.state.today_cashout}
                    </div>
                    <div className="output-total">
                        Last refresh: <br/>
                        {this.state.last_refresh}
                    </div>
                </div>
                <br/>
                <div className="item-grid">
                    {this.state.loading ? null : this.state.elements}
                </div>
            </section>
        )
    }
}

export default Inventory;