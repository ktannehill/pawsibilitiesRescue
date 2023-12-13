import { useDispatch, useSelector } from 'react-redux'
import { useEffect, useRef } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchOneEvent } from '../features/event/eventSlice'
import { fetchOnePet } from '../features/pet/petSlice'
import { fetchCurrentUser } from '../features/user/userSlice'
import toast from 'react-hot-toast'

const ViewOne = () => {
  const { entityType, id } = useParams()
  const data = useSelector(state => entityType === 'events' ? state.event.spotlight : state.pet.spotlight)
  const user = useSelector(state => state.user.data)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const prevIdRef = useRef()
  
  useEffect(() => {
    (async () => {
      if (id !== prevIdRef.current || !data) {
        try {
          if (entityType === 'events') {
              const { payload } = await dispatch(fetchOneEvent(id))
              if (typeof payload === 'string') {
                toast.error(payload)
                navigate('/')
              }
            } else if (entityType === 'pets') {
              const { payload } = await dispatch(fetchOnePet(id))
              if (typeof payload === 'string') {
                toast.error(payload)
                navigate('/')
              }
            } else {
              toast.error("Page does not exist")
              navigate('/')
            }
        } catch (error) {
            toast.error("Error fetching data:", error)
        }
      }
    })()
    prevIdRef.current = id
  },[data, id, dispatch, navigate, entityType])

  const handleAddEvent = (id) => {
    if (user.confirmed) {
      fetch("/volunteer", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ event_id: id }),
      })
      .then(resp => {
          if (resp.ok) {
              resp.json().then(data => {
                  toast.success("Successfully signed up for volunteer event!")
                  dispatch(fetchCurrentUser())
              })
          } else {
              resp.json().then(err => {
                  toast.error(err.message)
              })
          }
      })
      .catch(err => toast.error(err))
    } else{
      toast.error("Please confirm email before volunteering!")
    }
  }
  
  const handleFoster = (id) => {
    if (user.confirmed) {
      console.log(user)
    } else{
      toast.error("Please confirm email before fostering!")
    }
  }
  
  if (!data) { 
    return "Loading..."
  }

  return (
    <div id="main" className="layout-grid">
      <aside>
        <img src={data.image} alt={entityType === 'events' ? data.title : data.name} />
      </aside>
      <div className="grid-col-span-2">
        <h1>{entityType === 'events' ? data.title : data.name}</h1>
        {entityType === 'events' ? (
          <>
            <p>{data.location}</p>
            <p>{data.event_date}</p>
            <p>{data.description}</p>
            <button onClick={() => handleAddEvent(id)}>Volunteer</button>
          </>
        ) : (
          <>
            <p>{data.species}</p>
            <p>{data.breed}</p>
            <p>{data.est_birthday}</p>
            <p>{data.description}</p>
            <button onClick={handleFoster}>Foster</button>
          </>
        )}
      </div>
    </div>
  )
}

export default ViewOne