import React from "react"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"
import Plotly from "react-plotly.js"
import Plot from "react-plotly.js"

class InventoryStats extends React.Component {
    state = {
        x: null,
        y: null, 
        loading: false
    }

    async componentDidMount() {
        this.setState({loading: true})
        const url = "/api/inventory/stats"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": "76561198439884801"})
        })
        const data = await response.json()
        let x_data = []
        let y_data = []
        Object.keys(data).map((x) => {
            x_data.push(x)
            y_data.push(parseFloat(data[x]["todays_cashout"].split("$")[1]))
        })
        console.log(y_data)
        this.setState({loading: false, x: x_data})
    }
    render() {
        return(
            <div className="inventoryStats">
                <Navbar/>
                <InvBar/>
                <Plot
                    data={[
                        {
                            x: this.state.x,
                            y: this.state.y,
                            type: "scatter",
                            mode: "lines",
                            marker: {color: "red"},
                        }
                    ]}
                    layout={{width: 800, height: 740, title: 'Inventory Stats'}}
                />
            </div>
        )
    }
}

export default InventoryStats;