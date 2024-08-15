import React from "react";
import { useSelector } from "react-redux";

const Login = () => {
    const { user } = useSelector(state => state.user)
    return <div>
        Login
    </div>
}


export default Login;