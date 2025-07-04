<template>
  <div class="flex flex-col min-h-screen">
    <DashboardHeader />
    <main class="flex-grow">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import DashboardHeader from '../components/DashboardHeader.vue';
import AppFooter from '../components/AppFooter.vue'

export default {
  components: { DashboardHeader, AppFooter }
}
</script>
