import React from "react"
import QRCode from "qrcode.react"
import "./inventoryShare.scss"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryShare extends React.Component {
    copyLink = () => {

    }

    render() {
        return(
            <div className="Share" align="center">
                <Navbar title="History" steamid={this.props.match.params.steamid}/>
                <br/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <br/>
                <br/>
                <br/>
                <h4>Share your Inventory with your friends</h4>
                <QRCode value={window.location.href.replace("share/", "")} className="Qr-code" size="256"/>
                <h4 id="share-link">{window.location.href.replace("share/", "")}</h4>
                <button onClick={this.copyLink} id="copy-button">Copy</button>
            </div>
        )
    }
}

export default InventoryShare;