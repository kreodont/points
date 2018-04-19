// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import AWSAppSyncClient from "aws-appsync"
import VueApollo from 'vue-apollo'
import appSyncConfig from './AppSync'

Vue.config.productionTip = false;

const client = new AWSAppSyncClient({
  url: appSyncConfig.graphqlEndpoint,
  region: appSyncConfig.region,
  auth: {
    type: appSyncConfig.authenticationType,
    apiKey: appSyncConfig.apiKey,
  }
},{
  defaultOptions: {
    watchQuery: {
      fetchPolicy: 'cache-and-network',
    }
  }
});
console.log(client);

const appsyncProvider = new VueApollo({
  defaultClient: client
});
Vue.use(VueApollo);
/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  components: { App },
  provide: appsyncProvider.provide(),
  template: '<App/>'
});
