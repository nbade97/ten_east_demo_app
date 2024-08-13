import { createStore } from 'vuex';

const store = createStore({
  state: {
    projectName: '',
    amount: ''
  },
  mutations: {
    setProjectName(state, projectName) {
      state.projectName = projectName;
    },
    setAmount(state, amount) {
      state.amount = amount;
    }
  },
  actions: {
    updateProjectName({ commit }, projectName) {
      commit('setProjectName', projectName);
    },
    updateAmount({ commit }, amount) {
      commit('setAmount', amount);
    }
  },
  getters: {
    projectName: state => state.projectName,
    amount: state => state.amount
  }
});

export default store;