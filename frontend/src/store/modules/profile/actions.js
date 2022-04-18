import {
    axios
} from '../../../common/api.service.js';

export default {
    async getProfile(context) {
        let endpoint = '/api/v1/profile/';
        const response = await axios.get(endpoint);

        if (response.statusText !== 'OK') {
            console.log("profile/actions.js - BAD RESPONSE");
            const error = new Error("Response returned with the following status: " + response.status);
            throw error;
        }
        context.commit('setProfile', response.data)
    }
};