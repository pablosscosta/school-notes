<template>
  <header class="bg-gradient-to-t from-blue-500 to-blue-800 text-white p-4 shadow-md">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-2xl font-semibold">School Notes</h1>
      <nav class="space-x-4">
        <router-link to="/dashboard" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Meu Dashboard</router-link>
        <router-link to="/students" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Alunos</router-link>
        <router-link to="/classrooms" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Turmas</router-link>
        <router-link to="/subjects" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Disciplinas</router-link>
        <router-link to="/teachers" class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Professores</router-link>
        <router-link to="/"
        @click.native="handleLogout"
        class="px-3 py-1 rounded-md transition-colors duration-300 hover:bg-white hover:text-blue-700"
        >Sair</router-link>
      </nav>
    </div>
  </header>
</template>

<script>
import { logoutUser } from '@/services/auth';

export default {
  name: 'DashboardHeader',
  methods: {
    handleLogout(){
      logoutUser();
      this.$router.push('/');
    }
  },
};
</script>
