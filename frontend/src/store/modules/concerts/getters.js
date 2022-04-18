export default {
    events(state) {
        return state.events;
    },
    previousPageNumber(state) {
        return state.previousPageNumber;
    },
    nextPageNumber(state) {
        return state.nextPageNumber;
    },
    eventsCount(state) {
        return state.eventsCount;
    },
    eventsPerPage(state) {
        return state.eventsPerPage;
    },
    currentPageNumber(state) {
        return state.currentPageNumber;
    },
    currentSearchQuery(state) {
        return state.currentSearchQuery;
    },
    currentOrdering(state) {
        return state.ordering;
    }
}