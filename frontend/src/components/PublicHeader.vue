<template>
  <header class="bg-gradient-to-t from-blue-500 to-blue-800 text-white p-4 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-2xl font-semibold">School Notes</h1>
      <nav class="space-x-4">
        <router-link to="/" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Home</router-link>
        <router-link to="/login" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Login</router-link>
        <router-link to="/register" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Cadastro</router-link>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'PublicHeader',
}
</script>
