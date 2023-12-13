import { Link } from 'react-router-dom'

const Card = ({ item, entityType }) => {

    return (
        <div className="layout-grid">
            <aside className="card">
                <img src={item.image} alt={entityType === "events" ? item.title : item.name} />
            </aside>
            <div className="grid-col-span-2">
                <h2>{entityType === "events" ? item.title : item.name}</h2>
                <p>{item.description}</p>
                <Link to={`/${entityType === "events" ? "events" : "pets"}/${item.id}`}>
                    <button>See Details</button>
                </Link>
            </div>
        </div>
    )
}

export default Card