import {
    createStore
} from 'vuex';
import {
    axios
} from '../common/api.service';


import profileModule from './modules/profile/index.js';
import concertsModule from './modules/concerts/index.js';
import bandsModule from './modules/bands/index.js';

export default createStore({
    modules: {
        profile: profileModule,
        concerts: concertsModule,
        bands: bandsModule,
    },
    state() {
        return {
            userName: null,
            is_staff: false
        }
    },
    getters: {},
    actions: {
        async setUser() {
            const endpoint = '/api/v1/profile/';
            const response = await axios.get(endpoint);
            const username = response.data['user'];
            const is_staff = response.data['is_staff'];
            window.localStorage.setItem('username', username)
            window.localStorage.setItem('is_staff', is_staff)
            if (response.statusText !== 'OK') {
                console.log("index.js - setUser - BAD RESPONSE");
                const error = new Error("Response returned with the following status: " + response.status);
                throw error;
            }
        }

    },
    mutations: {}
});