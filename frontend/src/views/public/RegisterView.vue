<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 via-white to-emerald-50 p-4">
    <div class="bg-white shadow-xl rounded-xl p-8 w-full max-w-md transform hover:scale-[1.01] transition-transform duration-300">
      <h1 class="text-3xl font-semibold text-center text-gray-800 mb-6">Cadastro</h1>
      <form class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Nome</label>
          <input type="text" class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input type="email" class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500" />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Função</label>
          <select
            class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
            v-model="role"
          >
          <option value="" disabled selected>Selecione uma função</option>
          <option value="admin">Administrador</option>
          <option value="professor">Professor</option>
          <option value="aluno">Aluno</option>
          </select>
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Senha</label>
          <input type="password" class="w-full border border-gray-300 px-4 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500" />
        </div>
        <button type="submit" class="w-full bg-green-600 hover:bg-green-700 text-white py-2 rounded-lg text-lg font-medium transition-colors duration-300">
          Cadastrar
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterView',
  data() {
    return {
      role: '',
    }
  },
}
</script>
