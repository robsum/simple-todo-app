<template>
  <div class="todo-list">
    <h2>Todo List</h2>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.title }}
        <button @click="deleteTodo(todo.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>


<script>
import { mapActions, mapGetters } from 'vuex';

export default {
  data() {
    return {
      todos: [] // Initialize an empty array to hold the todo items
    };
  },
  mounted() {
    // Fetch todo items from the backend when the component is mounted
    this.fetchTodos();
  },
  computed: {
    ...mapGetters('todos', ['todos']),
  },
  methods: {
    ...mapActions('todos', ['fetchTodos', 'createTodo', 'deleteTodo']),
    async addTodo() {
      const newTodo = { title: 'Your New To-Do Task' }; // Replace with your actual todo data
      await this.createTodo(newTodo);
      await this.fetchTodos();
    },
    async fetchTodos() {
      try {
        const response = await fetch('http://backend:5000/todos');
        if (response.ok) {
          this.todos = await response.json(); // Update the todos array with the fetched data
          this.$store.commit('todos/setTodos', this.todos);
          console.log('TodoList:fetchTodos():response.ok');
        } else {
          console.error('TodoList:fetchTodos():Failed to fetch todos');
        }
      } catch (error) {
        console.error('TodoList:fetchTodos():An error occurred while fetching todos:', error);
      }
    },
    async deleteTodo(todoId) {
      try {
        await this.deleteTodo(todoId); // Dispatch the 'deleteTodo' action with the todo ID
        await this.fetchTodos(); // Fetch the updated todo list
      } catch (error) {
        console.error('Failed to delete todo:', error);
      }
    },
  },
};
</script>


<style>
.todo-list {
  background-color: #f0f0f0;
  padding: 16px;
  border-radius: 8px;
}

h2 {
  font-size: 24px;
  margin-bottom: 16px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  font-size: 18px;
  margin: 8px 0;
}
</style>
