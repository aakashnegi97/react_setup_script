import Dashboard from "../pages/dashboard"
import Login from "../pages/login"

export const publicRoutes = [
    {
        path: "/login",
        element: Login
    },
    // Default Route
    {
        path: "*",
        naviageTo: "/login"
    }
]

export const privateRoutes = [
    {
        path: "/dashboard",
        element: Dashboard
    },
    // Default Route
    {
        path: "*",
        naviageTo: "/dashboard"
    }
]