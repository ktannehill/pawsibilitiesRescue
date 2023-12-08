import { useState, useEffect } from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";
import AlertBar from "./components/AlertBar";
import Footer from "./components/Footer";

const App = () => {
    const [message, setMessage] = useState(null);
    const [snackType, setSnackType] = useState("");
    const [user, setUser] = useState(null); 

    useEffect(() => { 
        fetch("/check_session")
        .then((resp) => { 
            if (resp.ok) { 
                resp.json().then(setUser); 
            } else {
                resp.json().then(errorObj => {
                    handleSnackType("error")
                    setAlertMessage(errorObj.message)
                })
            }
        })
        .catch(errorObj => {
            handleSnackType("error")
            setAlertMessage(errorObj.message)
        })
    }, []);

    const updateUser = (user) => {setUser(user)}

    const setAlertMessage = (msg) => setMessage(msg);

    const handleSnackType = (type) => setSnackType(type);

    return (
        <div>
            <Header />
            {message && (
                <AlertBar
                    message={message}
                    snackType={snackType}
                    setAlertMessage={setAlertMessage}
                    handleSnackType={handleSnackType}
                />
            )}
            <div id="outlet">
                <Outlet />
            </div>
            <Footer />
        </div>
    )
}

export default App