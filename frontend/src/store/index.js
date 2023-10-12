import { createStore } from 'vuex';
import todos from './modules/todos'; // Import your todos module

export default createStore({
  modules: {
    todos, // Add your todos module to the store
    // You can add more modules if needed
  },
});