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
  // {
  //   path: '/articleSet/:title', // 每一个article-set的title等于原始视频的标题，不用担心会有同名现象；但是每一个article是llm生成的，因此可能会重复，所以用的不是title而是id
  //   name: "ArticleSet",
  //   component: () => import("@/views/article-set/index.vue")
  // },
  // {
  //   path: '/articleSetList/:theme',
  //   name: "ArticleSetList",
  //   component: () => import("@/views/article-set-list/index.vue")
  // },
  // {
  //   path: '/searchResult',
  //   name: "SearchResult",
  //   component: () => import("@/views/search-result/index.vue")
  // }
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
