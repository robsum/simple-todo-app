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
    removeTodo(state, todoId) {
      const index = state.todos.findIndex((todo) => todo.id === todoId);
      if (index !== -1) {
        state.todos.splice(index, 1);
      }
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
        await this.dispatch('fetchTodos');
      }, 1000);

    },

    async deleteTodo({ commit }, todoId) {
      try {
        const response = await fetch(`/todos/${todoId}`, {
          method: 'DELETE',
        });
  
        if (response.ok) {
          // Delete was successful, you can commit a mutation to remove it from the state
          commit('removeTodo', todoId);
        } else {
          console.error('Failed to delete todo');
        }
      } catch (error) {
        console.error('An error occurred while deleting a todo:', error);
      }
    },

  };
  
  export default {
    namespaced: true,
    state,
    mutations,
    actions,
  };
  