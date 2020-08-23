import React from  "react"
import "./errorDiv.scss"

class ErrorDiv extends React.Component {
    render() {
        return(
            <div className="ErrorDiv">
                <h1>Server error {this.props.statusCode}</h1>
            </div>
        )
    }
}

export default ErrorDiv;