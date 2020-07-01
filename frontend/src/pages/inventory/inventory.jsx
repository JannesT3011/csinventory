import React from "react"
import Navbar from "../../components/navbar/navbar"
import "./inventory.scss"
import InvBar from "../../components/invNavBar/invNavbar"
import Loading from "../../components/loading/loading"

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
        //const data = await response.json()
        this.setState({loading: false})
        window.location.reload()
    }

    async componentDidMount() { // change color of inventory button (invNav)
        var element = document.getElementById("inventory-point")
        element.style.backgroundColor = "#fff"
        element.style.color = "#353535"
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
    // {this.state.loading ? <Loading/> : <button onClick={this.updateInventory} className="update">Update!</button>} <br/> <br/> 
    render() { // TODO loading_button: if not loaded show normal button (statt null), if loaded show loading button
        return (
            <section className="Inventory">
                <Navbar/>
                <br/>
                <InvBar/>
                <div align="center">
                    <h1>Your Inventory:</h1>
                </div>
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
                </div>
                <br/>
                <div className="item-grid">
                    {this.state.elements}
                </div>
            </section>
        )
    }
}

export default Inventory;