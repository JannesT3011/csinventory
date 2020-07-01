import React from "react"
import "./loading.scss"

class Loading extends React.Component {
    render() { 
        return(
            <button className="update">
                <i className="fa fa-spinner fa-spin"></i> Updating...
            </button>
        )
    }
}

export default Loading;