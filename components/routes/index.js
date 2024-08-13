import React from "react";
import { BrowserRouter as Router } from 'react-router-dom';
import PublicRoutes from "./PublicRoutes";
import PrivateRoutes from "./PrivateRoutes";

const RootRouter = ({ isAuth }) => {
    return (
        <Router>
            {isAuth ? <PrivateRoutes /> : <PublicRoutes />}
        </Router>
    )
}
export default RootRouter;