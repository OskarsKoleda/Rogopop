import mutations from './mutations.js';
import actions from './actions.js'
import getters from './getters.js'

export default {
    namespaced: true,
    state() {
        return {
            events: [],
            currentSearchQuery: '',
            previousPageNumber: null,
            currentPageNumber: null,
            nextPageNumber: null,
            eventsCount: null,
            eventsPerPage: null,
            ordering: '',
        }
    },
    mutations,
    actions,
    getters
};