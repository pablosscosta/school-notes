<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-t from-gray-100 to-gray-300 p-4">
    <div class="bg-white shadow-xl rounded-xl p-12 w-full max-w-4xl mx-4 transform hover:scale-[1.02] transition-transform duration-300">
      <div class="space-y-6">
        <div class="flex items-center justify-between mb-6 flex-wrap gap-4">
            <h1 class="text-4xl font-semibold text-gray-800">
                Sobre o projeto School Notes
            </h1>

            <router-link to="/">
                <button class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 text-lg rounded-lg">
                Voltar
                </button>
            </router-link>
        </div>

        <div class="space-y-4 text-gray-700 leading-relaxed">
          <p class="text-lg">
            O School Notes é um sistema web para gerenciamento de alunos, turmas, disciplinas e notas.
            Ele foi desenvolvido com tecnologias modernas no frontend e backend, oferecendo uma solução prática
            e eficiente para escolas e instituições de ensino organizarem suas informações acadêmicas.
          </p>

          <div class="grid md:grid-cols-2 gap-6 mt-8">
            <div class="bg-gradient-to-br from-blue-50 to-indigo-50 p-6 rounded-lg border border-blue-100">
              <h3 class="text-xl font-semibold text-blue-800 mb-3">Funcionalidades</h3>
              <ul class="space-y-2 text-gray-700">
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
                  Gestão de alunos
                </li>
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
                  Controle de turmas
                </li>
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
                  Organização de disciplinas
                </li>
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-blue-500 rounded-full mr-3"></div>
                  Registro de notas
                </li>
              </ul>
            </div>

            <div class="bg-gradient-to-br from-green-50 to-emerald-50 p-6 rounded-lg border border-green-100">
              <h3 class="text-xl font-semibold text-green-800 mb-3">Tecnologias</h3>
              <ul class="space-y-2 text-gray-700">
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-green-500 rounded-full mr-3"></div>
                  Vue.js no Frontend
                </li>
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-green-500 rounded-full mr-3"></div>
                  Django no Backend
                </li>
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-green-500 rounded-full mr-3"></div>
                  Tailwind CSS
                </li>
                <li class="flex items-center">
                  <div class="w-2 h-2 bg-green-500 rounded-full mr-3"></div>
                  Design Responsivo
                </li>
              </ul>
            </div>
          </div>

          <div class="bg-gradient-to-r from-purple-50 to-pink-50 p-6 rounded-lg border border-purple-100 mt-8">
            <h3 class="text-xl font-semibold text-purple-800 mb-3">Objetivo</h3>
            <p class="text-gray-700">
              Facilitar a administração escolar através de uma interface intuitiva e moderna,
              permitindo que educadores foquem no que realmente importa: o ensino e aprendizado dos alunos.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutView'
}
</script>
