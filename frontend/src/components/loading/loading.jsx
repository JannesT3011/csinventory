import React from "react"
import "./loading.scss"
import * as Rb from "react-bootstrap"

class Loading extends React.Component {
    render() {
        return(
            <Rb.Spinner animation="border"/>
        )
    }
}

export default Loading;