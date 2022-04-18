export default {
    getFirstName(state) {
        return state.firstName;
    },
    getLastName(state) {
        return state.lastName;
    },
    getNumberOfEvents(state) {
        return state.concertsCount;
    },
    getTotalMoneySpent(state){
        return state.totalMoneySpent;
    }
}