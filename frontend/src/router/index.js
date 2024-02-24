import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);



export let routes = [
  {
    path: "/",
    redirect: "/theme",
  },
  {
    path: "/theme",
    name: "ThemeList",
    component: () => import("@/views/theme/index.vue"),
    children: [
      {
        path: "mental_health_and_addiction",
        name: "Theme_MentalHealthAndAddiction",
        component: () => import("@/views/theme/components/Theme.vue")
      },
      {
        path: "focus_productivity_and_creativity",
        name: "Theme_FocusProductivityAndCreativity",
        component: () => import("@/views/theme/components/Theme.vue")
      },
      {
        path: "the_science_of_well_being",
        name: "Theme_TheScienceOfWellBeing",
        component: () => import("@/views/theme/components/Theme.vue")
      }
    ]
  },
  {
    path: "/article_set/:themeTitle_en/:articleSetTitle_en",
    name: "ArticleSet",
    component: () => import("@/views/article_set/index.vue")
  },
  {
    path: '/article/:articleSetTitle_en/:articleSequence',
    name: "Article",
    component: () => import("@/views/article/index.vue")
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
