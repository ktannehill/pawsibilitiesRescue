import { Formik, Field, Form, ErrorMessage } from 'formik';
import { useDispatch, useSelector } from 'react-redux';
import * as Yup from 'yup';
import { fetchPatchEvent } from '../features/event/eventSlice'
import { fetchPatchPet } from '../features/pet/petSlice'
import toast from 'react-hot-toast'

const EditForm = ({ handleToggle, entityType }) => {
    const data = useSelector(state => entityType === 'events' ? state.event.spotlight : state.pet.spotlight)
    const dispatch = useDispatch()

    const initialValues = entityType === 'events' ? (
        {
            image: data.image,
            title: data.title,
            description: data.description,
            location: data.location,
            event_date: data.event_date
        }
    ) : (
        {
            image: data.image,
            name: data.name,
            species: data.species,
            breed: data.breed,
            sex: data.sex,
            description: data.description,
            est_birthday: data.est_birthday,
        }
    )

    const eventSchema = Yup.object().shape({
        image: Yup.string()
        .required("Please enter an image link"),
        title: Yup.string()
        .required("Please enter a title")
        .min(5, "Must be at least 5 characters"),
        description: Yup.string()
        .required("Please enter a description")
        .min(100, "Must be at least 100 characters"),
        location: Yup.string()
        .required("Please enter a location")
        .min(5, "Must be at least 5 characters"),
        event_date: Yup.date()
        .required("Please enter a date"),
    })
    const petSchema = Yup.object().shape({
        image: Yup.string()
        .required("Please enter an image link"),
        name: Yup.string()
        .required("Please enter a name")
        .min(1, "Must be at least 1 characters"),
        species: Yup.string()
        .required("Please enter a species")
        .min(3, "Species must be 'cat' or 'dog'"),
        breed: Yup.string()
        .required("Please enter a breed")
        .min(1, "Must be at least 1 characters"),
        sex: Yup.string()
        .required("Please enter a sex")
        .min(3, "Sex must be 'female' or 'male'"),
        description: Yup.string()
        .required("Please enter a description")
        .min(100, "Must be at least 100 characters"),
        est_birthday: Yup.date()
        .required("Please enter a date")
    })

    const CustomInputComponent = (props) => (
        <textarea rows="6" {...props} />
    )

    const id = data.id

    return (
        <Formik
        initialValues={initialValues}
        validationSchema={entityType === 'events' ? eventSchema : petSchema}
        onSubmit={async (values) => {
            if (entityType === 'events') {

                values["event_date"] = values.event_date.replace("T", " ")

                const {payload} = await dispatch(fetchPatchEvent({id, values}))
                if (typeof payload !== "string") {
                    handleToggle(false)
                    toast.success("Event updated")
                } else {
                    toast.error(payload)
                }
            } else if (entityType === 'pets') {
                const {payload} = await dispatch(fetchPatchPet({id, values}))
                if (typeof payload !== "string") {
                    handleToggle(false)
                    toast.success("Pet updated")
                } else {
                    toast.error(payload)
                }
            }
        }}
        >
        <Form>
            <div>
                <label htmlFor="image">Image</label>
                <Field name="image" type="text" placeholder="Image" className="block" />
                <ErrorMessage name="image" component="span" className="block error_msg" />

                {entityType === 'events' ? (
                    <>
                        <label htmlFor="title">Title</label>
                        <Field name="title" type="text" placeholder="Title" className="block" />
                        <ErrorMessage name="title" component="span" className="block error_msg" />
                    </>
                ) : (
                    <>
                        <label htmlFor="name">Name</label>
                        <Field name="name" type="text" placeholder="Name" className="block" />
                        <ErrorMessage name="name" component="span" className="block error_msg" />
                    </>
                )}

                <label htmlFor="description">Description</label>
                <Field name="description" as={CustomInputComponent} placeholder="Description" className="block" />
                <ErrorMessage name="description" component="span" className="block error_msg" />

                {entityType === 'events' ? (
                    <>
                        <label htmlFor="location">Location</label>
                        <Field name="location" type="text" placeholder="Location" className="block" />
                        <ErrorMessage name="location" component="span" className="block error_msg" />
                        
                        {/* <div className="flex_container">
                            <label htmlFor="date">Event Date
                            <Field name="date" type="date" className="block" />
                            <ErrorMessage name="date" component="span" className="block error_msg" />
                            </label>
                            
                            <label htmlFor="time">Event Time
                            <Field name="time" type="time" className="block" />
                            <ErrorMessage name="time" component="span" className="block error_msg" />
                            </label>
                        </div> */}

                        <label htmlFor="event_date">Event Date and Time</label>
                        <Field name='event_date' type='datetime-local' className="block" />
                        <ErrorMessage name='event_date' component="span" className="block error_msg" />

                    </>
                ) : (
                    <>
                    <div className="flex_container">
                        <label htmlFor="species">Species
                        <Field name="species"  as="select" className="block">
                            <option value="">Select one</option>
                            <option value="cat">cat</option>
                            <option value="dog">dog</option>
                        </Field>
                        <ErrorMessage name="species" component="span" className="block error_msg" />
                        </label>

                        <label htmlFor="breed">Breed
                        <Field name="breed" type="text" placeholder="Breed" className="block" />
                        <ErrorMessage name="breed" component="span" className="block error_msg" />
                        </label>
                    </div>
                    <div className="flex_container">
                        <label htmlFor="sex">Sex
                        <Field name="sex" as="select" className="block">
                            <option value="">Select one</option>
                            <option value="female">female</option>
                            <option value="male">male</option>
                        </Field>
                        <ErrorMessage name="sex" component="span" className="block error_msg" />
                        </label>

                        <label htmlFor="est_birthday">Birthdate
                        <Field name="est_birthday" type="date" className="block" />
                        <ErrorMessage name="est_birthday" component="span" className="block error_msg" />
                        </label>
                    </div>
                    </>
                )}
            </div>

            <div className="flex_container">
                <button type="submit">Submit</button>
                <button onClick={() => handleToggle(false)}>Cancel</button>
            </div>
        </Form>
        </Formik>
    );
};

export default EditForm