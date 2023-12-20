import { useDispatch, useSelector } from 'react-redux'
import { useEffect, useRef, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchOneEvent, fetchDeleteEvent } from '../features/event/eventSlice'
import { fetchOnePet, fetchDeletePet } from '../features/pet/petSlice'
import { fetchCurrentUser } from '../features/user/userSlice'
import toast from 'react-hot-toast'
import EditForm from '../components/EditForm'
import { GiMale, GiFemale } from "react-icons/gi"

const ViewOne = () => {
  const { entityType, id } = useParams()
  const data = useSelector(state => entityType === 'events' ? state.event.spotlight : state.pet.spotlight)
  const user = useSelector(state => state.user.data)
  const [edit, setEdit] = useState(false)
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const prevIdRef = useRef()

  const handleToggle = (val) => setEdit(val)
  
  useEffect(() => {
    (async () => {
      if (id !== prevIdRef.current || !data) {
        // make delete flag so this doesn't fire if true
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

  const confirmEvent = (id) => {
    return fetch(`/event_confirmation_email/${id}`)
      .then(resp => {
        if (resp.ok) {
          return resp.json()
        } else {
          throw new Error('Failed to send confirmation email')
        }
      })
  }

  const handleAddEvent = (id) => {
    if (user) {
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
            return resp.json()
          } else {
            throw new Error('Failed to sign up for volunteer event')
          }
        })
        .then(() => confirmEvent(id))
        .then(() => {
          toast.success("Successfully signed up for volunteer event! Check email for details.")
          dispatch(fetchCurrentUser())
          dispatch(fetchOneEvent(id))
        })
        .catch(err => {
          console.log(err)
          toast.error(err.message)
        });
      } else{
        toast.error("Please confirm email before volunteering!")
      }
    } else{
      toast.error("Please log in or sign up!")
      navigate("/login")
    }
  }

  const handleRemoveEvent = (id) => {
    fetch(`/volunteer_by_id/${id}`, {
      method: 'DELETE',
    })
    .then(resp => {
        if (resp.ok) {
            resp.json().then(data => {
                toast.success("No longer signed up for volunteer event.")
                dispatch(fetchOneEvent(id))
                dispatch(fetchCurrentUser())
            })
        } else {
            resp.json().then(err => {
                toast.error(err.message)
            })
        }
    })
    .catch(err => toast.error(err))
  }
  
  const handleFoster = (id) => {
    if(user) {
      if (user.confirmed) {
        toast.error("Feature coming soon!")
      } else{
        toast.error("Please confirm email before fostering!")
      }
    } else{
      toast.error("Please log in or sign up!")
      navigate("/login")
    }
  }

  const handleDelete = async () => {
    if (entityType === 'events') {
      const {payload} = await dispatch(fetchDeleteEvent(id))
      if (typeof payload !== "string") {
        navigate("/events")
        toast.success("Event deleted")
      } else {
        toast.error(payload)
      }
    } else if (entityType === 'pets') {
      const {payload} = await dispatch(fetchDeletePet(id))
      if (typeof payload !== "string") {
        navigate("/pets")
        toast.success("Pet deleted")
      } else {
        toast.error(payload)
      }
    }
  }
  
  if (!data) { 
    return "Loading..."
  }

  return (
    <>
      {edit ? (
        <main id="form">
          <h2>Edit {entityType === 'events' ? "Event" : "Pet"}</h2>
          <EditForm handleToggle={handleToggle} entityType={entityType} />
        </main>
      ) : (
        <>
          <div id="container">
            <div className="layout-grid">
              <aside>
                <img src={data.image} alt={entityType === 'events' ? data.title : data.name} />
              </aside>
              <main className="grid-col-span-2">
                <h1>{entityType === 'events' ? data.title : data.name}</h1>
                {entityType === 'events' ? (
                  <>
                    <p>{data.location}</p>
                    {/* <p>{data.formatted_date_short}</p> */}
                    <p>{data.formatted_date_full}</p>
                    <p>{data.description}</p>

                    <div className="flex_container">
                      {user && data.users?.find(data_user => data_user["id"] === user.id) ? (
                        <button onClick={() => handleRemoveEvent(id)}>Remove</button>
                      ) : (
                        <button onClick={() => handleAddEvent(id)}>Volunteer</button>
                      )}
                      {user && user.admin && (
                        <div className="flex_container">
                          <button onClick={() => handleToggle(true)}>Edit</button>
                          <button onClick={handleDelete}>Delete</button>
                        </div>
                      )}
                    </div>

                    <p>{data.users.length} Volunteers</p>
                    {data.users.length && user && user.admin ? (
                        <ul>
                          {data.users.map(user => (
                            <li key={user.id}>{user.username}</li>
                          ))}
                        </ul>
                    ) : null}
                  </>
                ) : (
                  <>
                    <p>{data.sex === "female" ? <GiFemale /> : <GiMale />} {data.breed}</p>
                    <p>
                      {data.age_years ? (
                        <span>{data.age_years} years </span>
                      ) : null}  
                      {data.age_months ? (
                        <span>{data.age_months} months </span>
                      ) : null} 
                      {!data.age_years && data.age_weeks ? (
                        <span>{data.age_weeks} weeks </span>
                      ) : null} 
                    </p>
                    <p>{data.description}</p>

                    <div className="flex_container">
                      <button onClick={handleFoster}>Foster</button>
                      {user && user.admin && (
                        <div className="flex_container">
                          <button onClick={() => handleToggle(true)}>Edit</button>
                          <button onClick={handleDelete}>Delete</button>
                        </div>
                      )}
                    </div>
                  </>
                )}
              </main>
            </div>
          </div>
        </>
      )}
    </>
  )
}

export default ViewOne