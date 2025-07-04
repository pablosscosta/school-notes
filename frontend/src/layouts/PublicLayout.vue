<template>
  <div class="flex flex-col min-h-screen">
    <PublicHeader />
    <main class="flex-grow">
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import PublicHeader from '../components/PublicHeader.vue'
import AppFooter from '../components/AppFooter.vue'

export default {
  components: { PublicHeader, AppFooter }
}
</script>
