import { createRouter, createWebHistory } from "vue-router";
import CheckIn from "../views/CheckIn.vue";
import Reports from "../views/Reports.vue";

const routes = [
  {
    path: "/",
    component: CheckIn,
  },
  {
    path: "/reports",
    component: Reports,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
