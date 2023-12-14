import { Formik, Field, Form, ErrorMessage } from 'formik';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import * as Yup from 'yup';
import { fetchRegister } from '../features/user/userSlice'
import toast from 'react-hot-toast'

const FormComp = ({ url }) => {
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
        password: Yup.string()
          .min(8, 'Must be at least 8 characters')
          .required('Required'),
      })}
      onSubmit={async (values) => {
          const action = await dispatch(fetchRegister({url, values}))
        if (typeof action.payload !== "string") {
          toast.success(`Welcome ${action.payload.username}!`)
          toast.success("A confirmation email has been sent.")
          navigate("/")
        } else {
          toast.error(action.payload)
        }
      }}
    >
      <Form>
        <div>
          <label htmlFor="first_name">First name</label>
          <Field name="first_name" type="text" className="block" />
          <ErrorMessage name="first_name" component="span" className="block error_msg" />

          <label htmlFor="last_name">Last name</label>
          <Field name="last_name" type="text" className="block" />
          <ErrorMessage name="last_name" component="span" className="block error_msg" />

          <label htmlFor="username">Username</label>
          <Field name="username" type="text" className="block" />
          <ErrorMessage name="username" component="span" className="block error_msg" />

          <label htmlFor="email">Email Address</label>
          <Field name="email" type="email" className="block" />
          <ErrorMessage name="email" component="span" className="block error_msg" />

          <label htmlFor="password">Password</label>
          <Field name="password" type="password" className="block" />
          <ErrorMessage name="password" component="span" className="block error_msg" />
        </div>

          <button type="submit">Submit</button>
      </Form>
    </Formik>
  );
};

export default FormComp