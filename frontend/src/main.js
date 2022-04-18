import {
    createApp
} from 'vue';
import App from './App.vue';
import router from './router.js';
import store from './store/index.js';

import BaseSpinner from './components/ui/BaseSpinner.vue';
import BaseModal from './components/ui/BaseModal.vue';


const app = createApp(App);
app.use(router);
app.use(store);

app.component('base-spinner', BaseSpinner);
app.component('base-modal', BaseModal);

app.mount('#app');