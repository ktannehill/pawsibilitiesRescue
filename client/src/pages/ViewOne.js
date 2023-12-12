import { useDispatch, useSelector } from 'react-redux'
import { useEffect, useRef } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchOneEvent } from '../features/event/eventSlice'

const ViewOne = () => {
  const event = useSelector(state => state.event.spotlight)
  const user = useSelector(state => state.user.data)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const { id } = useParams()
  const prevIdRef = useRef()
  
  useEffect(() => {
    (async () => {
      if (id !== prevIdRef.current || !event) {
        const {payload} = await dispatch(fetchOneEvent(id))
        if (typeof payload !== "string") {
          // console.log(payload)
        } else {
          console.log(payload)
          navigate("/")
        }
      }
    })()
    prevIdRef.current = id
  },[event, id, dispatch, navigate])

  const handleAddEvent = (id) => {
    if (user) {
      console.log(user)
    }
  }
  
  if (!event) { 
    return "Loading..."
  }

  const { image, title, description, location, event_date } = event

  return (
    <div id="main" className="layout-grid">
      <aside>
        <img src={image} alt={title} />
      </aside>
      <div className="grid-col-span-2">
        <h1>{title}</h1>
        <p>{location}</p>
        <p>{event_date}</p>
        <p>{description}</p>
        <button onClick={handleAddEvent}>Volunteer</button>
      </div>
    </div>
  )
}

export default ViewOne