<template>
  <div class="todo-form">
    <h3>Create New Todo</h3>
    <form @submit.prevent="createTodo">
      <input v-model="newTodo" type="text" placeholder="Enter a new todo" required />
      <button type="submit">Add</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTodo: '' // Initialize an empty string to hold the new todo
    };
  },
  methods: {
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
          const createdTodo = await response.json();
          this.$store.commit('todos/addTodo', createdTodo); // Commit the mutation to update the state
          this.$emit('todo-created', true); // Emit an event to notify the parent component
          this.$store.dispatch('todos/fetchTodos');
        } else if (response.status == 500) {
          console.log('TodoForm:createTodo():response500');
          this.$emit('todo-created', true);
          this.$store.dispatch('todos/fetchTodos');
        } else {
          console.error('TodoForm:createTodo():Failed to create a todo');
          this.$emit('todo-created', false);
        }
      } catch (error) {
        console.error('TodoForm:createTodo():An error occurred while creating a todo:', error);
        this.$emit('todo-created', false); // Emit 'false' for failure
      }
    }
  }
};
</script>

<style>
.todo-form {
  background-color: #f0f0f0;
  padding: 16px;
  border-radius: 8px;
  margin-top: 16px;
}

h3 {
  font-size: 20px;
  margin-bottom: 12px;
}

form {
  display: flex;
  flex-direction: column;
}

input {
  padding: 8px;
  margin-bottom: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
}

button {
  background-color: #007BFF;
  color: white;
  padding: 8px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
