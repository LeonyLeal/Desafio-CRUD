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
        @click="overlay = !overlay"
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
        @click="contatoOverlay = !contatoOverlay"
      >
        contato
      </v-btn>

      <v-overlay :z-index="zIndex" :value="overlay">
        <v-btn class="white--text" color="error" @click="overlay= false" absolute right top fab small>
          x
        </v-btn>
        <TaskNew />
      </v-overlay>
      <v-overlay :z-index="zIndex" :value="contatoOverlay">
        <v-btn class="white--text" color="error" @click="contatoOverlay= false" absolute right top fab small>
          x
        </v-btn>
        <ContatoNew/>
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
import ContatoNew from './components/ContatoNew.vue';
import TaskList from "./components/TaskList";
import TaskNew from "./components/TaskNew.vue";

export default {
  name: "App",

  components: {
    TaskList,
    TaskNew,
    ContatoNew,
  },

  data: () => ({
    overlay: false,
    contatoOverlay: false,
    zIndex: 10,
  }),
};
</script>
