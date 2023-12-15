import { useEffect, useMemo } from "react";
import { Outlet } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { fetchCurrentUser, clearErrors as clearUserErrors } from './features/user/userSlice'
import { clearErrors as clearEventErrors } from './features/event/eventSlice'
import { clearErrors as clearPetErrors } from './features/pet/petSlice'
import { Toaster } from 'react-hot-toast';
import toast from 'react-hot-toast'

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
          if (!user) {
            try {
              dispatch(fetchCurrentUser())
            }
            catch (error) {
              toast.error('Server is not available. Please try again later.');
            }
          }
        })()
      }, [user, dispatch])

      useEffect(() => {
        if (errors.length) {
            dispatch(clearUserErrors(""))
            dispatch(clearEventErrors(""))
            dispatch(clearPetErrors(""))
        }
      }, [errors, dispatch])

    return (
        <div id="flex">
            <Header />
            <Toaster/>
            <div id="outlet">
                <Outlet />
            </div>
            <Footer />
        </div>
    )
}

export default App