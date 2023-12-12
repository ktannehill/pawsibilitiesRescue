import { useSelector, useDispatch } from 'react-redux'
import { useNavigate, Link } from 'react-router-dom'
import Card from '../../components/Card'
import { fetchDeleteUser } from './userSlice'
import toast from 'react-hot-toast'
import { useState } from 'react'
import UserEdit from './UserEdit'

const Profile = () => {
    const user = useSelector(state => state.user.data)
    const [edit, setEdit] = useState(false)
    const dispatch = useDispatch()
    const navigate = useNavigate()

    const handleToggle = (val) => setEdit(val)

    const handleDelete = async () => {
        const {payload} = await dispatch(fetchDeleteUser(user.id))
        if (typeof payload !== "string") {
          toast.success("Profile deleted")
          navigate("/")
        } else {
          toast.error(payload)
        }
    }

    if (!user) { 
        return "Loading..."
    }

    return (
        <div>
            {edit ? (
                <div  id="container">
                    <h2 className='form'>Edit Profile</h2>
                    <UserEdit handleToggle={handleToggle} />
                </div>
            ) : (
                <>
                    <div id="banner">
                        <img src="https://images.unsplash.com/photo-1545658969-19d8799171f3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Person working on computer while cat sits in front of the screen" />
                        <h2>{user.username}</h2>
                    </div>
                    <main>
                        <div id="container">
                            {!user.confirmed && <p>Please confirm your email</p>}
                            <h2>{user.first_name} {user.last_name}</h2>
                            <div className="flex_container">
                                <button onClick={() => handleToggle(true)}>Edit</button>
                                <button onClick={handleDelete}>Delete</button>
                            </div>
                        </div>

                        {user.events.length ? (
                            <>
                            <div className="form">
                                <p>Your volunteer events</p>
                            </div>
                                {user.events.map(event => (
                                    <Card  key={event.id} event={event} />
                                ))}
                            </>
                        ) : (
                            <div id="container">
                                <p>It doesn't look like you have any events yet! Check them out on the Volunteer page.</p>
                            </div>
                        )}
                    </main>
                </>
            )}
        </div>
    )
}

export default Profile