import React from "react"
import QRCode from "qrcode.react"
import "./inventoryShare.scss"
import Navbar from "../../components/navbar/navbar"
import InvBar from "../../components/invNavBar/invNavbar"

class InventoryShare extends React.Component {
    copyLink = () => {
        var copyText = document.getElementById("share-link")
        copyText.select()
        copyText.setSelectionRange(0, 99999)
        document.execCommand("copy")
    }

    render() {
        return(
            <div className="Share" align="center">
                <Navbar title="History" steamid={this.props.match.params.steamid}/>
                <br/>
                <InvBar steamid={this.props.match.params.steamid}/>
                <br/>
                <h4>Share your Inventory with your friends</h4>
                <QRCode value={window.location.href.replace("share/", "")} className="Qr-code" size="200"/> 
                <br/>
                <br/>
                <input type="text" value={window.location.href.replace("share/", "")} id="share-link" readOnly/> <br/>
                <button onClick={this.copyLink} id="copy-button">Copy!</button>
            </div>
        )
    }
}

export default InventoryShare;