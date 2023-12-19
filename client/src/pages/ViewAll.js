import { useDispatch, useSelector } from 'react-redux'
import { useEffect, useState } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchAllEvents } from '../features/event/eventSlice'
import { fetchAllPets } from '../features/pet/petSlice'
import Card from '../components/Card'
import toast from 'react-hot-toast'

const ViewAll = () => {
    const { entityType } = useParams()
    const data = useSelector(state => entityType === 'events' ? state.event.data : state.pet.data)
    const [searchTerm, setSearchTerm] = useState("")
    const [sortOption, setSortOption] = useState("date")
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

    const handleSearch = (e) => {
        setSearchTerm(e.target.value)
    }

    const handleSortChange = (e) => {
        setSortOption(e.target.value)
    }

    const filteredData = data?.filter(item =>
        item.description?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.title?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.location?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        item.breed?.toLowerCase().includes(searchTerm.toLowerCase())
    )

    const sortedData = filteredData?.sort((a, b) => {
        if (sortOption === "date") {
            return new Date(a.event_date) - new Date(b.event_date)
        } else if (sortOption === "volunteers") {
            return a.users.length - b.users.length
        }
        return 0
    })

    const mappedItems = sortedData?.map(item => (
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
            {entityType === 'events' ? (
                    <p>
                        Volunteering at pet rescue events is a vital and valued contribution to our mission of finding loving homes for animals in need. Whether you're cleaning bowls, taking pets for walks, or dedicating a day to an adoption event, each effort plays a crucial role in creating a positive environment for these pets. We encourage members of our community to sign up for volunteer opportunities, as every small act of kindness adds up to make a significant impact. Your involvement ensures that these animals receive the care and attention they deserve, bringing them one step closer to finding their forever homes. Join us in making a difference and being a source of compassion for these wonderful pets.
                    </p>
                ) : (
                    <p>
                        All our rescue pets available for foster or adoption are provided with the utmost care. They are spayed or neutered and kept up-to-date on age-appropriate vaccinations, ensuring their overall well-being. As a volunteer, if you choose to foster a pet that may require medical treatment, rest assured that our rescue group is committed to providing the necessary care and support. Your dedication to fostering not only provides a safe haven for these pets but also contributes to their journey towards a healthier and happier life. Join us in making a positive impact on the lives of these animals, knowing that your efforts directly contribute to their well-rounded care and eventual placement in loving homes.
                    </p>
                )}
                <div className='flex_container'>
                    <label htmlFor="search">
                        <input
                            name="search"
                            type="text"
                            placeholder={`Search ${entityType === 'events' ? 'events' : 'pets'}`}
                            value={searchTerm}
                            onChange={handleSearch}
                            className='block'
                        /> 
                    </label>
                    <label htmlFor="sort_by">
                        <select value={sortOption} onChange={handleSortChange}>
                            <option value="">Sort by:</option>
                            <option value="date">Date</option>
                            <option value="volunteers">Volunteers</option>
                        </select>
                    </label>
                </div>
                {data && mappedItems}
            </main>
        </div>
  )
}

export default ViewAll