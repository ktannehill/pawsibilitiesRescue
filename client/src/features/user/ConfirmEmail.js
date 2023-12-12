import { useEffect } from 'react'
import { Formik, Field, Form, ErrorMessage } from 'formik';
import * as Yup from 'yup';
import toast from 'react-hot-toast'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate, useParams } from 'react-router-dom'
import { fetchRegister } from './userSlice'

const ConfirmEmail = () => {
    const user = useSelector(state => state.user.data)
    const { token } = useParams()
    const navigate = useNavigate()
    const dispatch = useDispatch()

    useEffect(() => {
        fetch(`/confirm_email/${token}`)
        .then(resp => {
            if (resp.ok) {
                resp.json().then(data => {
                    toast.success("Email confirmed, please log in!")
                })
            } else {
                resp.json().then(err => {
                    toast.error(err)
                })
            }
        })
    }, [])

    const url = "/user_login"

    return (
        <div id="container" className="center">
            <Formik
            initialValues={{ 
              username: '', 
              password: '' }
            }
            validationSchema={Yup.object({
              username: Yup.string()
                .min(5, 'Must be at least 5 characters')
                .required('Required'),
              password: Yup.string()
                .min(8, 'Must be at least 8 characters')
                .required('Required'),
            })}
            onSubmit={async (values) => {
              const action = await dispatch(fetchRegister({url, values}))
              if (typeof action.payload !== "string") {
                toast.success(`Welcome ${action.payload.username}!`)
                navigate("/")
              } else {
                toast.error(action.payload)
              }
            }}
          >
            <Form>
                <label htmlFor="username">Username or Email</label>
                <Field name="username" type="text" className="block" />
                <ErrorMessage name="username" className="block" />

                <label htmlFor="password">Password</label>
                <Field name="password" type="password" className="block" />
                <ErrorMessage name="password" className="block" />

                <button type="submit">Submit</button>
            </Form>
          </Formik>
        </div>
    )
}

export default ConfirmEmail