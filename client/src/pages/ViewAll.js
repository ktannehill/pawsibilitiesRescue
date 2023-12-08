import { useSelector } from 'react-redux'
import Card from '../components/Card'

const ViewAll = () => {
    const events = useSelector(state => state.events)
    // const pets = useSelector(state => state.pets)

    const mappedEvents = events.map(item => (
        <Card key={item.id} {...item} />
    ))

    return (
        <div>
            <div id="banner">
                <img src="https://images.unsplash.com/photo-1571325654970-9c00c5432fcb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Two smiling people each holding a dog" />
                <h2>Sign up for one of our events today!</h2>
            </div>
            <div id="container">
                {mappedEvents}
            </div>
        </div>
  )
}

export default ViewAll