import { Formik, Field, Form, ErrorMessage } from 'formik';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import * as Yup from 'yup';
import { fetchPatchUser } from './userSlice'
import toast from 'react-hot-toast'

const UserEdit = ({ handleToggle }) => {
  const user = useSelector(state => state.user.data)
  const dispatch = useDispatch()
  const navigate = useNavigate()

  const {id, first_name, last_name, username, email} = user

  return (
    <Formik
      initialValues={{ 
        first_name: first_name, 
        last_name: last_name, 
        username: username, 
        email: email}
      }
      validationSchema={Yup.object({
        first_name: Yup.string()
          .min(1, 'Must be at least 1 characters')
          .matches(/^[A-Za-z]+$/, 'Must contain only alphabetic letters')
          .required('Required'),
        last_name: Yup.string()
          .min(1, 'Must be at least 1 characters')
          .matches(/^[A-Za-z]+$/, 'Must contain only alphabetic letters')
          .required('Required'),
        username: Yup.string()
          .min(5, 'Must be at least 5 characters')
          .required('Required'),
        email: Yup.string().email('Invalid email address').required('Required'),
      })}
      onSubmit={async (values) => {
        const action = await dispatch(fetchPatchUser({id, values}))
        if (typeof action.payload !== "string") {
          toast.success("Successfully updated profile.")
          navigate("/profile")
          handleToggle(false)
        } else {
          toast.error(action.payload)
        }
      }}
    >
      <Form>
        <div>
          <label htmlFor="first_name">First name</label>
          <Field name="first_name" type="text" className="block" />
          <ErrorMessage name="first_name" className="block" />

          <label htmlFor="last_name">Last name</label>
          <Field name="last_name" type="text" className="block" />
          <ErrorMessage name="last_name" className="block" />

          <label htmlFor="username">Username</label>
          <Field name="username" type="text" className="block" />
          <ErrorMessage name="username" className="block" />

          <label htmlFor="email">Email Address</label>
          <Field name="email" type="email" className="block" />
          <ErrorMessage name="email" className="block" />

          {/* <label htmlFor="password">Password</label>
          <Field name="password" type="password" className="block" />
          <ErrorMessage name="password" className="block" /> */}
        </div>

        <div className="flex_container">
          <button type="submit">Submit</button>
          <button onClick={() => handleToggle(false)}>Cancel</button>
        </div>
      </Form>
    </Formik>
  );
};

export default UserEdit