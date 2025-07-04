<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-white to-purple-50 p-4">
    <div class="bg-white shadow-xl rounded-xl p-8 w-full max-w-md transform hover:scale-[1.01] transition-transform duration-300">
      <h1 class="text-3xl font-semibold text-center text-gray-800 mb-6">Login</h1>
      <form class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input type="email" class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Senha</label>
          <input type="password" class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </div>
        <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded-lg text-lg font-medium transition-colors duration-300">
          Entrar
        </button>
        <router-link to="/register">
          <button class="w-full bg-red-500 hover:bg-red-400 text-white py-2 rounded-lg text-lg font-medium transition-colors duration-300">
          Não tem conta? Cadastre-se aqui!
          </button>
        </router-link>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginView'
}
</script>
