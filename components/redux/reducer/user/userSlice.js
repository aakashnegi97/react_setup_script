import { createSlice } from '@reduxjs/toolkit';
import { userReducerActions } from './actions';

const initialState = {
    user: null,
    status: 'idle',
    error: null,
}

const userSlice = createSlice({
    name: 'users',
    initialState: initialState,
    reducers: {
        ...userReducerActions
    }
});

export const actions = userSlice.actions;

export default userSlice.reducer;
