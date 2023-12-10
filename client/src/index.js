import ReactDOM from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import routes from "./routes";
import "./index.css";
import { Provider } from "react-redux";
import { store } from "./app/store";

const router = createBrowserRouter(routes);

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Provider store={store}>
        <RouterProvider router={router} />
    </Provider>);