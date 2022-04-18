import {
    axios
} from '../../../common/api.service';

export default {
    async fetchOneEvent(context, eventlug) {
        let endpoint = `/api/v1/concert/${eventlug}/`;
        const response = await axios.get(endpoint);
        if (response.statusText !== 'OK') {
            console.log("concerts/actions.js - fetchOneEvent - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
        return response.data;
    },
    saveQueryValue(context, payload) {
        context.commit('setSearchQuery', payload);
    },
    storeOrdering(context, ordering) {
        context.commit('setOrdering', ordering)
    },
    async fetchEvents(context, payload) {
        context.dispatch('saveQueryValue', payload.searchString);
        let endpoint = '/api/v1/concerts/';
        const response = await axios.get(endpoint, {
            params: {
                page: payload.page,
                search: payload.searchString,
                ordering: payload.ordering
            }
        });

        if (response.statusText !== 'OK') {
            console.log("concerts/actions.js - fetchEvents - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
        context.commit('setEvents', response.data.results);
        context.commit('setNextPageNumber', response.data.next_page_number);
        context.commit('setPreviousPageNumber', response.data.previous_page_number);
        context.commit('setCurrentPageNumber', response.data.current_page_number);
        context.commit('setEventsCount', response.data.count);
        context.commit('setEventsPerPage', response.data.per_page);

    },
    async joinEvent(context, eventSlug) {
        const endpoint = `/api/v1/concerts/${eventSlug}/join/`;
        const response = await axios.post(endpoint);
        if (response.statusText !== 'OK') {
            console.log("concerts/actions.js - joinEvent - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
        context.commit('joinEvent', eventSlug)
    },
    async unjoinEvent(context, eventSlug) {
        const endpoint = `/api/v1/concerts/${eventSlug}/join/`;
        try {
            await axios.delete(endpoint);
        } catch (error) {
            console.log(error);
        }
        context.commit('unjoinEvent', eventSlug)
    },
    async updateEvent(_, payload) {
        const endpoint = `/api/v1/concert/${payload.slug}/`;
        const response = await axios.put(endpoint, payload.body, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        if (response.statusText !== 'OK') {
            console.log("concerts/actions.js - updateEvent - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
    },

    async addEvent(_, payload) {
        const endpoint = '/api/v1/concerts/';
        const response = await axios.post(endpoint, payload, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });
        if (response.statusText !== 'Created') {
            console.log(response);
            console.log("concerts/actions.js - updateEvent - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
    },

    async removeEvent(_, payload) {
        const endpoint = `/api/v1/concert/${payload}/`;
        const response = await axios.delete(endpoint);
        if (response.statusText !== 'No Content') {
            console.log("concerts/actions.js - removeEvent - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
    },
}