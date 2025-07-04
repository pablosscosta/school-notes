<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
    <div class="container mx-auto px-4 py-16">
      <!-- Título e descrição -->
      <div class="text-center mb-16">
        <div class="flex justify-center mb-6">
          <div class="bg-blue-600 p-4 rounded-full">
            <BookOpenIcon class="w-12 h-12 text-white" />
          </div>
        </div>
        <h1 class="text-5xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
          School Notes
        </h1>
        <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Sistema completo para gerenciamento escolar. Organize alunos, turmas, disciplinas e notas em uma plataforma moderna e intuitiva.
        </p>

        <router-link to="/about">
          <button class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 text-lg rounded-lg">
            Sobre o Projeto
          </button>
        </router-link>
      </div>

      <!-- Cards -->
      <div class="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
        <!-- Card 1 -->
        <div class="bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100">
          <div class="bg-blue-100 p-3 rounded-full w-fit mb-4">
            <TableCellsIcon class="w-8 h-8 text-blue-600"/>
          </div>
          <h3 class="text-xl font-semibold mb-3 text-gray-800">Gestão de Alunos</h3>
          <p class="text-gray-600">
            Cadastre e gerencie informações completas dos alunos de forma organizada e eficiente.
          </p>
        </div>

        <!-- Card 2 -->
        <div class="bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100">
          <div class="bg-green-100 p-3 rounded-full w-fit mb-4">
            <AcademicCapIcon class="w-8 h-8 text-green-600" />
          </div>
          <h3 class="text-xl font-semibold mb-3 text-gray-800">Controle de Turmas</h3>
          <p class="text-gray-600">
            Organize turmas e disciplinas com facilidade, mantendo tudo estruturado e acessível.
          </p>
        </div>

        <!-- Card 3 -->
        <div class="bg-white p-8 rounded-xl shadow-lg hover:shadow-xl transition-shadow duration-300 border border-gray-100">
          <div class="bg-purple-100 p-3 rounded-full w-fit mb-4">
            <ClipboardDocumentIcon class="w-8 h-8 text-purple-600" />
          </div>
          <h3 class="text-xl font-semibold mb-3 text-gray-800">Registro de Notas</h3>
          <p class="text-gray-600">
            Sistema completo para lançamento e acompanhamento de notas e avaliações dos estudantes.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  BookOpenIcon,
  ClipboardDocumentIcon,
  AcademicCapIcon,
  TableCellsIcon,
} from '@heroicons/vue/24/outline'

export default {
  name: 'HomeView',
  components: {
    BookOpenIcon,
    ClipboardDocumentIcon,
    AcademicCapIcon,
    TableCellsIcon,
  }
}
</script>
