<template>
  <div class="flex flex-col min-h-screen">
    <Navbar />
    <div class="flex-grow">
      <div class="relative mx-auto">
        <RouterView />
        <ChatbotFloatingBtn class="fixed bottom-4 right-4" />
      </div>
    </div>
  </div>
  <div id="app">
    <SilverPrice />
  </div>
</template>

<script setup>
import ChatbotFloatingBtn from '@/components/ChatbotFloatingBtn.vue';
import { RouterView } from 'vue-router';
import Navbar from '@/components/Navbar.vue';
import SilverPrice from './components/SilverPrice.vue';


</script>
