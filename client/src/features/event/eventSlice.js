import { buildCreateSlice, asyncThunkCreator } from "@reduxjs/toolkit"

export const createSlice = buildCreateSlice({
    creators: { asyncThunk: asyncThunkCreator }
})

const initialState = {
    data: null,
    spotlight: null,
    errors: [],
    loading: true
}

const fetchAll = async () => {
    try {
        const resp = await fetch("/events")
        const data = await resp.json()
        if (resp.ok) {
            return data
        } else {
            throw data.message
        }
    } catch (error) {
        return error
    }
}

const fetchOne = async (id, asyncThunk) => {
    try {
        const resp = await fetch(`/events/${id}`)
        const data = await resp.json()
        if (resp.ok) {
            return data
        } else {
            throw data.message
        }
    } catch (error) {
        return error
    }
}

// const postEvent = async (values, asyncThunk) => {
//     try {
//         const resp = await fetch("/events", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(values)
//         })
//         const data = await resp.json()
//         if (resp.ok) {
//             return data
//         } else {
//             throw data.message
//         }
//     } catch (error) {
//         return error
//     }
// }

// const patchEvent = async ({ id, values }, asyncThunk) => {
//     try {
//         const resp = await fetch(`/events/${id}`, {
//             method: "PATCH",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify(values)
//         })
//         const data = await resp.json()
//         if (resp.ok) {
//             return data
//         } else {
//             throw data.message || data.msg
//         }
//     } catch (error) {
//         return error
//     }
// }

// const deleteEvent = async (id, asyncThunk) => {
//     try {
//         const resp = await fetch(`/events/${id}`, {
//             method: "DELETE"
//         })
//         if (resp.ok) {
//             return { id }
//         } else {
//             const data = await resp.json()
//             throw data.message || data.msg
//         }
//     } catch (error) {
//         return error
//     }
// }

const eventSlice = createSlice({
    name: "event",
    initialState,
    reducers: (create) => ({
        setEvent: create.reducer((state, action) => {
            state.spotlight = action.payload
            state.loading = false
            state.errors = []
        }),
        addError: create.reducer((state, action) => {
            state.errors.push(action.payload)
        }),
        clearErrors: create.reducer((state) => {
            state.errors = []
        }),
        fetchAllEvents: create.asyncThunk(
            fetchAll,
            {
                pending: (state) => {
                    state.loading = true
                    state.errors = []
                },
                rejected: (state, action) => {
                    state.loading = false
                    state.errors.push(action.payload)
                },
                fulfilled: (state, action) => {
                    state.loading = false
                    state.data = action.payload
                }
            }
        ),
        fetchOneEvent: create.asyncThunk(
            fetchOne,
            {
                pending: (state) => {
                    state.loading = true
                    state.errors = []
                },
                rejected: (state, action) => {
                    state.loading = false
                    state.errors.push(action.payload)
                },
                fulfilled: (state, action) => {
                    state.loading = false
                    if (!action.payload.id) {
                        state.errors.push(action.payload)
                    } else {
                        state.spotlight = action.payload
                    }
                }
            }
        )
    }),
    selectors: {
        selectEvents(state){
            return state.data
        },
        selectErrors(state){
            return state.errors
        },
        selectEventById: (state, id) => {
            return state.data.find(event => event.id === id)
        }
    }
})

export const { setEvent, addError, clearErrors, fetchAllEvents, fetchOneEvent } = eventSlice.actions
export const { selectEvent, selectErrors } = eventSlice.selectors
export default eventSlice.reducer