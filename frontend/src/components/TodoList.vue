<template>
<div>
  <div class="todo-form">
    <h3>Create New Todo</h3>
    <form @submit.prevent="createTodo">
      <input v-model="newTodo" type="text" placeholder="Enter a new todo" required />
      <button type="submit">Add</button>
    </form>
  </div>
  <div class="todo-list">
    <h2>Todo List</h2>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        {{ todo.title }}
        <button @click="deleteTodoAction(todo.id)">Delete</button>
      </li>
    </ul>
  </div>
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
        const response = await fetch('/todos');
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
    async deleteTodoAction(todoId) {
      try {
        await this.deleteTodo(todoId); // Dispatch the 'deleteTodo' action with the todo ID
        await this.fetchTodos(); // Fetch the updated todo list
      } catch (error) {
        console.error('Failed to delete todo:', error);
      }
    },
    async createTodo() {
      try {
        const response = await fetch('/todos', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ title: this.newTodo })
        });
        if (response.ok) {
          console.log('TodoForm:createTodo():response.ok');
          this.newTodo = ''; // Clear the input field after successfully creating the todo
          await this.fetchTodos();
        } else if (response.status == 500) {
          console.log('TodoForm:createTodo():response500');
          this.newTodo = ''; 
          await this.fetchTodos();
        } else {
          console.error('TodoForm:createTodo():Failed to create a todo');
        }
      } catch (error) {
        console.error('TodoForm:createTodo():An error occurred while creating a todo:', error);
      }
    }
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
