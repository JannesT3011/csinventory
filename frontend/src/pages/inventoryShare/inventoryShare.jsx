import React from "react"
import QRCode from "qrcode.react"
import "./inventoryShare.scss"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryShare extends React.Component {
    render() {
        return(
            <div className="Share" align="center">
                <Navbar title="History" steamid={this.props.match.params.steamid}/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <br/>
                <br/>
                <br/>
                <br/>
                <QRCode value={window.location.href} className="Qr-code" size="256"/>
            </div>
        )
    }
}

export default InventoryShare;