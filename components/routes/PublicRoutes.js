import React from "react";
import { Navigate, Route, Routes } from 'react-router-dom';
import { publicRoutes } from "./config";

const PublicRoutes = () => {
    return (
        <Routes>
            {
                publicRoutes?.map((item, index) => {
                    return <Route
                        key={index}
                        path={item.path}
                        element={
                            item.element ?
                                <item.element />
                                : item?.naviageTo
                                    ? <Navigate to={item?.naviageTo} />
                                    : null
                        } />
                })
            }

        </Routes>
    )
}
export default PublicRoutes;