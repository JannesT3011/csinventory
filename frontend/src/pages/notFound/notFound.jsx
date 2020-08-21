import React from "react"
import {Link} from "react-router-dom"

class NotFound extends React.Component {
    render() {
        return(
            <div className="NotFound">
                <h1>404</h1>
                <Link to="/">
                    Back home
                </Link>
            </div>
        )
    }
}

export default NotFound;