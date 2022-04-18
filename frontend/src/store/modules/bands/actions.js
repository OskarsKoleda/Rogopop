import {
    axios
} from '../../../common/api.service';

export default {

    async fetchBands(context) {
        let endpoint = '/api/v1/bands/';
        const response = await axios.get(endpoint);
        if (response.statusText !== 'OK') {
            console.log("concerts/actions.js - fetchOneEvent - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
        context.commit('setBands', response.data);
    }
}