import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', name: "Home", component: () => import("../views/Home.vue"), },
        { path: '/live', name: "LiveMonitor", component: () => import("../views/LiveMonitor.vue"), },
        { path: '/solve', name: "Solve", component: () => import("../views/Solve.vue"), },
        { path: '/runs', name: "Runs", component: () => import("../views/Runs.vue"), },
        { path: '/runs/:id', name: "RunReport", props: true, component: () => import("../views/RunReport.vue"), },
        { path: '/:pathMatch(.*)*', name: "NotFound", component: () => import("../views/NotFound.vue"), },
    ]
})

export default router