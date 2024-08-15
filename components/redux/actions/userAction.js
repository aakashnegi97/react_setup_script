import { actions } from "../reducer/user/userSlice"



// Action Methods Start
export const fetchUserData = (request) => {

    return async (dispatch, getState) => {
        dispatch(actions.updateUserData(request))
    }
}
// Action Methods End
