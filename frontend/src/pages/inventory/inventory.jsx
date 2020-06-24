import React from "react"
import Navbar from "../../components/navbar/navbar"
import "./inventory.scss"

class Inventory extends React.Component {
    state = {
        items: null,
        elements:null,
        today_cashout: null,
        inv_amount: null
    }

    async componentDidMount() {
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
                        <h1>{item}</h1>
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
            <div className="Inventory">
                <Navbar/>
                {this.state.inv_amount}
                {this.state.today_cashout}
                <h1>Inventory</h1>
                {this.state.elements}
            </div>
        )
    }
}

export default Inventory;