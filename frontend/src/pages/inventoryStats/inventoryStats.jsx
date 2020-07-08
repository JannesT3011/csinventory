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
        var element = document.getElementById("stats-point")
        element.style.backgroundColor = "#fff"
        element.style.color = "#353535"
        this.setState({loading: true})
        const url = "/api/inventory/stats"
        const response = await fetch(url, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"steamid": this.props.match.params.steamid})
        })
        const data = await response.json()
        let x_data = []
        let y_data = []
        Object.keys(data).map((x) => {
            x_data.push(x)
            y_data.push(parseFloat(data[x]["todays_cashout"].split("$")[1]))
        })
    
        this.setState({loading: false, x: x_data, y: y_data})
        console.log(this.state.y)
        console.log(this.state.x)
    }
    render() {
        return(
            <div className="inventoryStats">
                <Navbar title="Stats" steamid={this.props.match.params.steamid}/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <br/>
                <div align="center">
                <Plot
                    data={[
                        {
                            x: this.state.x,
                            y: this.state.y,
                            type: "scatter",
                            marker: {color: "red"}
                        }
                    ]}
                    layout={{title: "Inventory Stats", autosize:true}}
                    config={{responsive: true}}
                    />
                </div>
            </div>
        )
    }
}

export default InventoryStats;