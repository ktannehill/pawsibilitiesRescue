import { useDispatch, useSelector } from 'react-redux'
import { useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import { fetchAllEvents } from '../features/event/eventSlice'
import Card from '../components/Card'
import toast from 'react-hot-toast'

const ViewAll = () => {
    const events = useSelector(state => state.event.data)
    // const pets = useSelector(state => state.pets.data)
    const dispatch = useDispatch()
    const navigate = useNavigate()

    useEffect(() => {
        (async () => {
            if (!events) {
                const {payload} = await dispatch(fetchAllEvents())
                if (typeof payload !== "string") {
                    // console.log("VA18: ", payload)
                } else {
                    toast.error(payload)
                    navigate("/")
                }
            }
        })()
    },[events])

    const mappedEvents = events?.map(event => (
        <Card key={event.id} event={event} />
    ))

    return (
        <div>
            <div id="banner">
                <img src="https://images.unsplash.com/photo-1571325654970-9c00c5432fcb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Two smiling people each holding a dog" />
                <h2>Sign up for a volunteer event today!</h2>
            </div>
            <div>
                {events && mappedEvents}
            </div>
        </div>
  )
}

export default ViewAll