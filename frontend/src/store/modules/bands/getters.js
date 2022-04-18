export default {
    bandsList(state) {
        return state.bands.map(band => band.name);
    }
}