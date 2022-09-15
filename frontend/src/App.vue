<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <h2>Tarefas</h2>
    </v-app-bar>

    <v-main>
      <TaskList />
      <v-btn
        color="green"
        fab
        dark
        small
        fixed
        bottom
        right
        class="font-lg"
        @click="taskOverlay = !taskOverlay"
      >
        +
      </v-btn>
      <v-btn
        color="green"
        dark
        small
        fixed
        bottom
        left
        @click="contactOverlay = !contactOverlay"
      >
        contato
      </v-btn>

      <v-overlay :z-index="zIndex" :value="taskOverlay">
        <v-btn class="white--text" color="error" @click="TaskOverlay= false" absolute right top fab small>
          x
        </v-btn>
        <TaskNew />
      </v-overlay>
      <v-overlay :z-index="zIndex" :value="contactOverlay">
        <v-btn class="white--text" color="error" @click="contactOverlay= false" absolute right top fab small>
          x
        </v-btn>
        <ContactNew/>
      </v-overlay>
    </v-main>
  </v-app>
</template>

<style scoped>
.font-lg {
  font-size: 2rem;
  font-weight: 400;
}
</style>

<script>
import ContactNew from './components/ContactNew.vue';
import TaskList from "./components/TaskList";
import TaskNew from "./components/TaskNew.vue";

export default {
  name: "App",

  components: {
    TaskList,
    TaskNew,
    ContactNew,
  },

  data: () => ({
    taskOverlay: false,
    contactOverlay: false,
    zIndex: 100,
  }),
};
</script>
