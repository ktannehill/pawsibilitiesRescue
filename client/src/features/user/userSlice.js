import { buildCreateSlice, asyncThunkCreator } from "@reduxjs/toolkit"

export const createSlice = buildCreateSlice({
    creators: { asyncThunk: asyncThunkCreator }
})

const initialState = {
    data: null,
    errors: [],
    loading: true
}

const register = async ({ url, vals },) => {
    try {
        const resp = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(vals)
        })
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

const fetchUser = async () => {
    try {
        const resp = await fetch("/check_user", {
            headers: {
                "Content-Type": "application/json"
            }
        })
        const data = await resp.json()
        if (resp.ok) {
            return { user: data }
        } else {
            throw data.message
        }
    } catch (error) {
        return error
    }
}

const patchUser = async ({ id, vals }, asyncThunk) => {
    try {
        const resp = await fetch(`/users/${id}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(vals)
        })
        const data = await resp.json()
        if (resp.ok) {
            return data
        } else {
            throw data.message || data.msg
        }
    } catch (error) {
        return error
    }
}

const deleteUser = async (id, asyncThunk) => {
    try {
        const resp = await fetch(`/users/${id}`, {
            method: "DELETE"
        })
        if (resp.ok) {
            return { id }
        } else {
            const data = await resp.json()
            throw data.message || data.msg
        }
    } catch (error) {
        return error
    }
}

const userSlice = createSlice({
    name: "user",
    initialState,
    reducers: (create) => ({
        setUser: create.reducer((state, action) => {
            state.data = action.payload
            state.loading = false
            state.errors = []
        }),
        logout: create.reducer((state) => {
            state.data = null
            state.errors = []
        }),
        addError: create.reducer((state, action) => {
            state.errors.push(action.payload)
        }),
        clearErrors: create.reducer((state) => {
            state.errors = []
        }),
        fetchRegister: create.asyncThunk(
            register,
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
                    if (typeof action.pyload === "string") {
                        state.errors.push(action.payload)
                    } else {
                        state.data = action.payload
                    }
                }
            }
        ),
        fetchCurrentUser: create.asyncThunk(
            fetchUser,
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
                    if (typeof action.pyload === "string") {
                        state.errors.push(action.payload)
                    } else {
                        state.data = action.payload
                    }
                }
            }
        ),
        fetchPatchUser: create.asyncThunk(
            patchUser,
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
                    if (typeof action.pyload === "string") {
                        state.errors.push(action.payload)
                    } else {
                        state.data = action.payload
                    }
                }
            }
        ),
        fetchDeleteUser: create.asyncThunk(
            deleteUser,
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
                    if (typeof action.pyload === "string") {
                        state.errors.push(action.payload)
                    } else {
                        state.data = null
                    }
                }
            }
        ),
    }),
    selectors: {
        selectUser(state) {
            return state.data
        },
        selectErrors(state) {
            return state.errors
        }
    }
})

export const { setUser, logout, addError, clearErrors, fetchRegister, fetchCurrentUser, fetchPatchUser, fetchDeleteUser } = userSlice.actions
export const { selectUser, selectErrors } = userSlice.selectors
export default userSlice.reducer