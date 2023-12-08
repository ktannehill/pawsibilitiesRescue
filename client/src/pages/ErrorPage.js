import { Link } from 'react-router-dom'

const ErrorPage = () => {
  return (
    <div>
        <div id="banner">
                <img src="https://images.unsplash.com/photo-1450778869180-41d0601e046e?q=80&w=1886&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Cat head-butting dog in grass"/>
                <h2>Ruh-roh!</h2>
            </div>
            <div id="container">
                <h2>Could not find what you were looking for!</h2>
                <button>
                    <Link to="/">
                        Go home
                    </Link>
                </button>
            </div>
    </div>
  )
}

export default ErrorPage