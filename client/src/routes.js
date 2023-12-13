import App from "./App"
import ErrorPage from "./pages/ErrorPage"
import Home from "./pages/Home"
import Authentication from "./features/user/Authentication"
import Profile from "./features/user/Profile"
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
                path: "/login/:token",
                element: <Authentication />,
            },
            {
                path: "/profile",
                element: <Profile />,
            },
            {
                path: "/:entityType",
                element: <ViewAll />,
            },
            {
                path: "/:entityType/:id",
                element: <ViewOne />,
            },
            {
                path: "/:entityType",
                element: <ViewAll />,
            },
            {
                path: "/:entityType/:id",
                element: <ViewOne />,
            }
        ],
    },
];

export default routes;