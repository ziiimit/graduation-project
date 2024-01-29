import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);



export let routes = [
  {
    path: "/",
    redirect: "/home",
  },
  {
    path: "/home",
    name: "Home",
    component: () => import("@/views/home/index.vue"),
  },
  {
    path: '/articleSet/:title',
    name: "ArticleSet",
    component: () => import("@/views/article-set/index.vue")
  },
  {
    path: '/searchResult',
    name: "SearchResult",
    component: () => import("@/views/search-result/index.vue")
  }
];
const router = new VueRouter({
  mode: "history",
  routes: routes,
});


router.beforeEach((to, from, next) => {

  document.body.style.opacity = '0'

  document.body.addEventListener('transitionend', function routeAfterTransition() {
    next();
    document.body.removeEventListener('transitionend', routeAfterTransition)
  })
})

router.afterEach(() => {

  document.body.style.opacity = '1'
})

export default router;
