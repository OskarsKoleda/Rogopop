export default {
    setProfile(state, payload) {
        state.firstName = payload.first_name;
        state.lastName = payload.last_name;
        state.concertsCount = payload.events_count;
        state.totalMoneySpent = payload.money_spent;
    }
};