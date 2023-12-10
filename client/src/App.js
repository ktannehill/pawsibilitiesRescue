import { useEffect } from "react";
import { Outlet } from "react-router-dom";
import Header from "./components/Header";
import AlertBar from "./components/AlertBar";
import Footer from "./components/Footer";
import { useDispatch, useSelector } from "react-redux";
import { fetchCurrentUser } from './features/user/userSlice'

const App = () => {
    const user = useSelector(state => state.user.data)
    const userErrors = useSelector(state => state.user.errors)
    const dispatch = useDispatch()

    useEffect(() => {
        (async () => {
          if (!user) {
            const {payload} = await dispatch(fetchCurrentUser())
            if (typeof payload !== "string") {
                console.log("VA18: ", payload)
            } else {
                console.log("VA20: ", payload)
            }
          }
        })()
      }, [user])

    return (
        <div id="flex">
            <Header className="row" />
            {/* {message && (
                <AlertBar
                    message={message}
                    snackType={snackType}
                    setAlertMessage={setAlertMessage}
                    handleSnackType={handleSnackType}
                />
            )} */}
            <div id="outlet">
                <Outlet />
            </div>
            <Footer className="row" />
        </div>
    )
}

export default App