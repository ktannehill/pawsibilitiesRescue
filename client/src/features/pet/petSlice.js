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
        const resp = await fetch("/pets")
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
        const resp = await fetch(`/pets/${id}`)
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

const postPet = async (vals, asyncThunk) => {
    try {
        const resp = await fetch("/pets", {
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

const patchPet = async ({ id, vals }, asyncThunk) => {
    try {
        const resp = await fetch(`/pets/${id}`, {
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

const deletePet = async (id, asyncThunk) => {
    try {
        const resp = await fetch(`/pets/${id}`, {
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

const petSlice = createSlice({
    name: "pet",
    initialState,
    reducers: (create) => ({
        setPet: create.reducer((state, action) => {
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
        fetchAllPets: create.asyncThunk(
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
        fetchOnePet: create.asyncThunk(
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
        selectPets(state){
            return state.data
        },
        selectErrors(state){
            return state.errors
        },
        selectPetById: (state, id) => {
            return state.data.find(pet => pet.id === id)
        }
    }
})

export const { setPet, addError, clearErrors, fetchAllEPes, fetchOnePet } = petSlice.actions
export const { selectPet, selectErrors } = petSlice.selectors
export default petSlice.reducer