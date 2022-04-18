import {
  createRouter,
  createWebHistory
} from 'vue-router'
import Home from './pages/home/Home.vue';
import Profile from './pages/profile/Profile.vue';
import Concerts from './pages/events/concerts/Concerts.vue';

const routes = [{
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/profile',
    name: 'profile',
    component: Profile
  },
  {
    path: '/events',
    name: 'events',
    component: () => import('./pages/events/Events.vue'),
    children: [{
        path: 'concerts/:page?',
        name: 'concerts',
        component: Concerts
      },
      {
        path: 'concert/add',
        name: 'concert-creator',
        component: () => import('./pages/events/concerts/ConcertEditor.vue')
      },
      {
        path: 'concert/:slug',
        name: 'concert-details',
        props: true,
        component: () => import('./pages/events/concerts/ConcertDetails.vue')
      },
      {
        path: 'bands',
        name: 'bands',
        component: () => import('./pages/events/bands/Bands.vue')
      },
    ]
  },
  {
    path: '/concert/:slug/edit',
    name: 'concert-editor',
    component: () => import('./pages/events/concerts/ConcertEditor.vue')
  },

  {
    path: '/:notFound(.*)',
    component: () => import('./pages/404.vue')
  }


  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router