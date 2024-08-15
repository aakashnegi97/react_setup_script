import React from "react";
import { BrowserRouter as Router } from 'react-router-dom';
import PublicRoutes from "./PublicRoutes";
import PrivateRoutes from "./PrivateRoutes";
import PrivateLayout from "../components/layout/PrivateLayout";
import PublicLayout from "../components/layout/PublicLayout";

const RootRouter = ({ isAuth }) => {
    return (
        <Router>
            {isAuth ?
                <PrivateLayout>
                    <PrivateRoutes />
                </PrivateLayout> :
                <PublicLayout>
                    <PublicRoutes />
                </PublicLayout>
            }
        </Router>
    )
}
export default RootRouter;