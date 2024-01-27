import Vue from "vue";
import App from "./App.vue";



Vue.config.productionTip = false;


import "@/style/normalize.css"
import "@/style/index.scss"


import store from "@/store";
import router from "@/router";


import axios from "axios";



new Vue({
  render: (h) => h(App),
  store,
  router,
}).$mount("#app");
