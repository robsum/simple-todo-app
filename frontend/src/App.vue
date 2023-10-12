<template>
  <div id=app>
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <TodoForm @todo-created="handleTodoCreated" />
    <TodoList />
  </div>
</template>

<script>
import TodoForm from './components/TodoForm.vue';
import TodoList from './components/TodoList.vue'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList
  },
  methods: {
    async handleTodoCreated(success) {
      console.log("handleTodoCreated() in App.vue");
      if (success) {
        // This method is called when a new todo is created
        // You can perform any additional actions here if needed
        console.log('App:handleTodoCreated():Todo created successfully');
        // const todoListComponent = this.$children.find((child) => child.$options.name === 'TodoList');
        // if (todoListComponent) {
        //     todoListComponent.fetchTodos();
        // } else {
        //     console.error('TodoList component not found among child components.');
        // }
        //await this.$store.dispatch('todos/fetchTodos');
      } else {
        console.log('App:handleTodoCreated():Failed to create a todo');
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
