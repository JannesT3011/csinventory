import React from "react"
import Navbar from "../../components/navbar/navbar"
import "./inventory.scss"
import InvBar from "../../components/invNavBar/invNavbar"
import Loading from "../../components/loading/loading"

import Spinner from "react-bootstrap/Spinner"

class Inventory extends React.Component {
    state = {
        items: null,
        elements:null,
        today_cashout: null,
        inv_amount: null,
        loading: false
    }

    updateInventory = async() => {
        this.setState({loading: true})
        const url = "/api/inventory/refresh/76561198439884801"
        const response = await fetch(url)
        const data = await response.json()
        this.setState({loading: false})
        window.location.reload()
    }

    async componentDidMount() { // hier auch loading screen machen
        const url = "/api/inventory"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": "76561198439884801", "update": false})
        })
        const data = await response.json()
        console.log(data)
        this.setState({items: data})
        let elements = []

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
        

        this.setState({elements:elements, today_cashout:data["todays_cashout"], inv_amount: data["inventory_amount"]})
        setInterval(response, 5000)
    }

    render() {
        return (
            <section className="Inventory">
                <Navbar/>
                <InvBar/>
                <button onClick={this.updateInventory}>Update!</button>
                {this.state.loading ? <Loading/> : null}
                {this.state.inv_amount}
                {this.state.today_cashout}
                <h1>Inventory</h1>
                <div className="item-grid">
                    {this.state.elements}
                </div>
            </section>
        )
    }
}

export default Inventory;