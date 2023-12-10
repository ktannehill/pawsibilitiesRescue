import { configureStore } from "@reduxjs/toolkit"
import userReducer from "../features/user/userSlice"
import eventReducer from "../features/event/eventSlice"
import petReducer from "../features/pet/petSlice"

export const store = configureStore({
    reducer: {
        user: userReducer,
        event: eventReducer,
        pet: petReducer
    },
    devTools: {trace: true}
})