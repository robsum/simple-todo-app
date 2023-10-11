<template>
  <div class="todo-list">
    <h2>Todo List</h2>
    <ul>
      <li v-for="todo in todos" :key="todo.id">{{ todo.title }}</li>
    </ul>
  </div>
</template>

<script>
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
  methods: {
    async fetchTodos() {
      try {
        const response = await fetch('http://srv16.mikr.us:20112/todos');
        if (response.ok) {
          this.todos = await response.json(); // Update the todos array with the fetched data
        } else {
          console.error('Failed to fetch todos');
        }
      } catch (error) {
        console.error('An error occurred while fetching todos:', error);
      }
    }
  }
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
