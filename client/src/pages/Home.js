import React from 'react'

const Home = () => {
  return (
    <div>
        <div id="banner">
            <img src="https://images.unsplash.com/photo-1565979748550-c1dc4e262945?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Close up for happy dog being pet be out-of-frame owner at park" />
            <h2>Creating a paw-sitive impact!</h2>
        </div>
        <div id="main" className="layout-grid">
            <article className="grid-col-span-2">
                <p>
                    Paw-sibilities Rescue is more than just a shelter; we are a community dedicated to creating a world where every animal has the opportunity for a loving home. Our mission is to ease the burden on local shelters by providing a caring and nurturing space for animals in need. With a commitment to compassion and hope, we strive to eliminate the need for euthanasia in shelters, working tirelessly to place each precious life in a forever home.
                </p>
                <p>
                    At Paw-sibilities Rescue, we believe in the power of love to transform lives. Through our dedicated team and community of volunteers, we inspire paws-itivity and invite everyone to join us on this journey. Together, we can make a difference in the lives of animals, one paw at a time.
                </p>
            </article>
            <aside>
                <img src="https://images.unsplash.com/photo-1601758003081-cc85332409de?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" alt="Happy couple holding their adopted cat at home" />
            </aside>
        </div>
    </div>
  )
}

export default Home