import { useDispatch, useSelector } from 'react-redux'
import { useEffect } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchAllEvents } from '../features/event/eventSlice'
import { fetchAllPets } from '../features/pet/petSlice'
import Card from '../components/Card'
import toast from 'react-hot-toast'

const ViewAll = () => {
    const { entityType } = useParams()
    const data = useSelector(state => entityType === 'events' ? state.event.data : state.pet.data)
    const dispatch = useDispatch()
    const navigate = useNavigate()

    useEffect(() => {
        (async () => {
            if (!data) {
                try {
                    if (entityType === 'events') {
                        const { payload } = await dispatch(fetchAllEvents())
                        if (typeof payload === 'string') {
                          toast.error(payload)
                          navigate('/')
                        }
                      } else if (entityType === 'pets') {
                        const { payload } = await dispatch(fetchAllPets())
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
    },[data, dispatch, navigate, entityType])

    const mappedEvents = data?.map(item => (
        <Card key={item.id} item={item} entityType={entityType} />
    ))

    return (
        <div>
            <div id="banner">
                {entityType === 'events' ? (
                    <>
                        <img src="https://images.unsplash.com/photo-1571325654970-9c00c5432fcb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Two smiling people each holding a dog" />
                        <h2>Sign up for a volunteer event today!</h2>
                    </>
                ) : (
                    <>
                        <img src="https://images.unsplash.com/photo-1520560321666-4b36560e7979?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Cat from above getting back scratched" />
                        <h2>Meet our adorable adoptable pets!</h2>
                    </>
                )}
            </div>
            <main id="container">
                {data && mappedEvents}
            </main>
        </div>
  )
}

export default ViewAll