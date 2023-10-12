// store/modules.todos.js

const state = {
    todos: [],
  };
  
  const mutations = {
    setTodos(state, todos) {
      state.todos = todos;
    },
    addTodo(state, todo) {
      state.todos.push(todo);
      console.log('New todo added:', todo); // Add this line to log the added todo
    },
  };
  
  const actions = {
    async fetchTodos({ commit }) {
      // Make an API request to get the list of todos from the backend.
      const response = await fetch('/todos');
      const todos = await response.json();
      commit('setTodos', todos);
    },
    async createTodo({ commit }, todoData) {
      // Make an API request to create a new todo on the backend.
      const response = await fetch('/todos', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(todoData),
      });
      const createdTodo = await response.json();
      
      // Simulate a delay of 1 second before fetching the updated list
      setTimeout(async () => {
        commit('addTodo', createdTodo);
        await fetchTodos({ commit });
      }, 1000);

    },
  };
  
  export default {
    namespaced: true,
    state,
    mutations,
    actions,
  };
  