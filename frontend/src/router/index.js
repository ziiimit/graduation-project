import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);



export let routes = [
  {
    path: "/",
    redirect: "/Home",
  },
  {
    path: "/Home",
    name: "Home",
    component: () => import("@/views/home/index.vue")
  },
  {
    path: '/Theme/:themeTitle_en',
    name: 'Theme',
    component: () => import("@/views/theme/index.vue")
  },
  {
    path: "/ArticleSet/:themeTitle_en/:articleSetTitle_en",
    name: "ArticleSet",
    component: () => import("@/views/article_set/index.vue")
  },
  {
    path: '/Article/:articleSetTitle_en/:articleSequence',
    name: "Article",
    component: () => import("@/views/article/index.vue")
  },
  {
    path: '/search_result',
    name: "SearchResult",
    component: () => import("@/views/search_result/index.vue")
  },

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
