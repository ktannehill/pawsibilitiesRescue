import { Formik, Field, Form, ErrorMessage } from 'formik';
import { useDispatch } from 'react-redux'
import { useNavigate, useParams } from 'react-router-dom';
import * as Yup from 'yup';
import { fetchRegister } from './userSlice'
import { useEffect, useState } from 'react';
import FormComp from "../../components/FormComp";
import toast from 'react-hot-toast'

const Authentication = () => {
  const [login, setLogin] = useState(true)
  const { token } = useParams()
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const handleClick = () => setLogin((login) => !login)

  const url = login ? "/user_login" : "/signup"

  useEffect(() => {
    if (token) {
      fetch(`/confirm_email/${token}`)
      .then(resp => {
        if (resp.ok) {
          resp.json().then(data => {
            toast.success("Email confirmed, please log in!")
          })
        } else {
          resp.json().then(err => {
            toast.error(err.message)
          })
        }
      })
      .catch(err => toast.error(err.message))
    }
}, [token])

  return (
    <div id="form">
      {login ? (
        <>
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
                <ErrorMessage name="username" component="span" className="block error_msg" />

                <label htmlFor="password">Password</label>
                <Field name="password" type="password" className="block" />
                <ErrorMessage name="password" component="span" className="block error_msg" />

                <button type="submit">Submit</button>
            </Form>
          </Formik>
          <div className="form">
            <h2>Don't have an account?</h2>
            <button onClick={handleClick}>Sign up</button>
          </div>
        </>
      ) : (
        <FormComp url={url} />
      )}
    </div>
  )
}

export default Authentication