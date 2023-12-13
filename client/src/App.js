import { useEffect, useMemo } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import Header from "./components/Header";
// import AlertBar from "./components/AlertBar";
import Footer from "./components/Footer";
import { fetchCurrentUser } from './features/user/userSlice'
import { clearErrors as clearUserErrors} from './features/user/userSlice'
import { Toaster } from 'react-hot-toast';

const App = () => {
    const user = useSelector(state => state.user.data)
    const userErrors = useSelector(state => state.user.errors)
    const eventErrors = useSelector(state => state.event.errors)
    const petErrors = useSelector(state => state.pet.errors)
    const errors = useMemo(() => [...userErrors, ...eventErrors, ...petErrors], [
      userErrors,
      eventErrors,
      petErrors,
    ]);
    const dispatch = useDispatch()

    useEffect(() => {
        (async () => {
          if (!user) {dispatch(fetchCurrentUser())}
        })()
      }, [user, dispatch])

      useEffect(() => {
        if (errors.length) {
            dispatch(clearUserErrors(""))
        }
      }, [errors, dispatch])

    return (
        <div id="flex">
            <Header className="row" />
            <Toaster/>
            <div id="outlet">
                <Outlet />
            </div>
            <Footer className="row" />
        </div>
    )
}

export default App