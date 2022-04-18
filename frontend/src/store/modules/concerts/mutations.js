export default {
    setEvents(state, payload) {
        state.events = payload;
    },
    setPreviousPageNumber(state, payload) {
        state.previousPageNumber = payload;
    },
    setCurrentPageNumber(state, payload) {
        state.currentPageNumber = payload;
    },
    setNextPageNumber(state, payload) {
        state.nextPageNumber = payload;
    },
    setEventsCount(state, payload) {
        state.eventsCount = payload;
    },
    setEventsPerPage(state, payload) {
        state.eventsPerPage = payload;
    },
    joinEvent(state, payload) {
        const index = state.events.findIndex(event => event.slug === payload)
        state.events[index]['user_has_participated'] = true
    },
    unjoinEvent(state, payload) {
        const index = state.events.findIndex(event => event.slug === payload)
        state.events[index]['user_has_participated'] = false
    },
    setSearchQuery(state, payload) {
        state.currentSearchQuery = payload;
    },
    setOrdering(state, payload) {
        state.ordering = payload;
    }
};