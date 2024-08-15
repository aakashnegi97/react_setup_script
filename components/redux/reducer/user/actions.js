export const userReducerActions = {
    updateUserData: (state, action) => {
        state.user = action.payload;
        state.status = 'succeeded';
    },
    updateUserLoading: (state, action) => {
        state.status = action.payload ? 'loading' : 'idle';
    },
    updateUserError: (state, action) => {
        state.error = action.payload;
        state.status = 'failed';
    },
}