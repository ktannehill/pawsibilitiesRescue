import { useSelector, useDispatch } from 'react-redux'
import { useNavigate } from 'react-router-dom'
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

    const handleResend = () => {
        fetch(`/resend_confirmation_email/${user.id}`)
        .then(resp => {
            if (resp.ok) {
                resp.json().then(data => {
                    toast.success("Confirmation email resent successfully")
                })
            } else {
                resp.json().then(err => {
                    toast.error(err)
                })
            }
        })
        .catch(err => toast.error(err))
    }

    if (!user) { 
        return "Loading..."
    }

    return (
        <>
            {edit ? (
                <main  id="form">
                    <h2>Edit Profile</h2>
                    <UserEdit handleToggle={handleToggle} />
                </main>
            ) : (
                <>
                    <div id="banner">
                        <img src="https://images.unsplash.com/photo-1545658969-19d8799171f3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Person working on computer while cat sits in front of the screen" />
                        <h2>{user.username}</h2>
                    </div>
                    <main id="container">
                        {!user.confirmed && (
                            <div className="flex_container">
                                <p>Please confirm your email</p>
                                <button onClick={handleResend}>Resend Link</button>
                            </div>
                        )}
                        <div className="flex_container">
                            <h2>{user.first_name} {user.last_name}</h2>
                            <div className="flex_container">
                                <button onClick={() => handleToggle(true)}>Edit</button>
                                <button onClick={handleDelete}>Delete</button>
                            </div>
                        </div>

                        {user.events.length ? (
                            <>
                            <h3>Your volunteer events</h3>
                            {user.events.map(item => (
                                <Card  key={item.id} item={item} entityType="events" />
                            ))}
                            </>
                        ) : (
                            <p>It doesn't look like you have any events yet! Check them out on the Volunteer page.</p>
                        )}
                    </main>
                </>
            )}
        </>
    )
}

export default Profile