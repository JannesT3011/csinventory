import React from "react"
import {Link} from "react-router-dom"
import "./notFound.scss"

class NotFound extends React.Component {
    render() {
        return(
            <div className="NotFound">
                <div class="NotFound-middle">
                  <div class="NotFount-inner">
                    <h4>404</h4>
                    <h1>Page not found</h1>
                    <hr/>
                    <br/>
                    <a href="/">Go back home!</a>
                  </div>
                </div>
            </div>
        )
    }
}

export default NotFound;