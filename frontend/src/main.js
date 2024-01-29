import Vue from "vue";
import App from "./App.vue";



Vue.config.productionTip = false;


import "@/style/normalize.css"
import "@/style/index.scss"


import store from "@/store";
import router from "@/router";


import axios from 'axios';
axios.defaults.baseURL = "http://127.0.0.1:5000";


new Vue({
  render: (h) => h(App),
  store,
  router,
}).$mount("#app");
