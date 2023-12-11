import { Formik, Field, Form, ErrorMessage } from 'formik';
import { useDispatch, useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import * as Yup from 'yup';
import { fetchPatchUser, fetchRegister } from '../features/user/userSlice'

const FormComp = () => {
  const user = useSelector(state => state.user.data)
  const dispatch = useDispatch()
  const navigate = useNavigate()

  return (
    <Formik
      initialValues={{ 
        first_name: '', 
        last_name: '', 
        username: '', 
        email: '', 
        password: '' }
      }
      validationSchema={Yup.object({
        first_name: Yup.string()
          .min(1, 'Must be at least 1 characters')
          .required('Required'),
        last_name: Yup.string()
          .min(1, 'Must be at least 1 characters')
          .required('Required'),
        username: Yup.string()
          .min(5, 'Must be at least 5 characters')
          .required('Required'),
        email: Yup.string().email('Invalid email address').required('Required'),
        password: Yup.string()
          .min(8, 'Must be at least 8 characters')
          .required('Required'),
      })}
      onSubmit={async (values) => {
        // if (user) {
        //   let id = user.id
        //   const action = await dispatch(fetchPatchUser({id, values}))
        // } else {
          const action = await dispatch(fetchRegister({values}))
        // }
        if (typeof action.payload !== "string") {
          console.log(action.payload)
          navigate("/")
        } else {
          console.log(action.payload)
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

          <label htmlFor="password">Password</label>
          <Field name="password" type="password" className="block" />
          <ErrorMessage name="password" className="block" />
        </div>

          <button type="submit">Submit</button>
      </Form>
    </Formik>
  );
};

export default FormComp