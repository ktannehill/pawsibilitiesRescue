import { Link } from 'react-router-dom'

const Card = ({ event }) => {
    const { id, image, title, description } = event
    return (
        <div className="layout-grid">
            <aside className="card">
                <img src={image} alt={title} />
            </aside>
            <div className="grid-col-span-2">
                <h2>{title}</h2>
                <p>{description}</p>
                <Link to={`/events/${id}`}>
                    <button>See Details</button>
                </Link>
            </div>
        </div>
    )
}

export default Card