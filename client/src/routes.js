import App from "./App"
import ErrorPage from "./pages/ErrorPage"
import Home from "./pages/Home"
import Authentication from "./pages/Authentication"
import Profile from "./pages/Profile"
import ViewAll from "./pages/ViewAll"
import ViewOne from "./pages/ViewOne"

const routes = [
    {
        path: "/",
        element: <App />,
        errorElement: <ErrorPage />,
        children: [
            {
                path: "/",
                index: true,
                element: <Home />,
            },
            {
                path: "/login",
                element: <Authentication />,
            },
            {
                path: "/profile/",
                element: <Profile />,
            },
            {
                path: "/profile/edit",
                element: <Authentication />,
            },
            {
                path: "/pets",
                element: <ViewAll />,
            },
            {
                path: "/pets/:id",
                element: <ViewOne />,
            },
            {
                path: "/events",
                element: <ViewAll />,
            },
            {
                path: "/events/:id",
                element: <ViewOne />,
            }
        ],
    },
];

export default routes;