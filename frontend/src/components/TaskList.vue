<template>
  <v-card max-width="450" class="mx-auto">
    <v-list three-line>
      <template v-for="task in tasks">
        <v-list-item :key="task.id">
          <v-col class="flex-grow-0 pa-0 pr-10 text-center">
            <p class="" v-html="task.contato_id"></p>
          </v-col>
          <v-list-item-content>
            <v-row class="ma-0">
              <v-list-item-title
                class="no-flex"
              ><strong>{{task.id}}-{{task.titulo}}</strong></v-list-item-title>
              <v-checkbox
                :input-value="task.ativo"
                class="ma-0 mt-4"
                @click="updateStatus(task)"
              ></v-checkbox>
            </v-row>
            <v-list-item-subtitle
              class="mb-16"
              v-html="task.descricao"
            ></v-list-item-subtitle>
            <v-row class="ma-0 float-rigth no-flex justify-end">
              <v-btn elevation="2" raised @click="overlay = !overlay">
                Editar</v-btn
              >
              <v-btn
                elevation="2"
                raised
                color="error"
                @click="taskDelete(task)"
              >
                Deletar</v-btn
              >
              <v-overlay :z-index="zIndex" :value="overlayDelete" class="ma-auto">
                <v-btn
                  class="white--text mr-5"
                  color="error"
                  @click="overlayDelete = false"
                >
                  Não deletar
                </v-btn>
                <v-btn
                  class="white--text"
                  color="error"
                  @click="overlayDelete = false"
                >
                Deletar
                </v-btn>
              </v-overlay>
              <v-overlay :z-index="zIndex" :value="overlay">
                <v-btn
                  class="white--text"
                  color="error"
                  @click="overlay = false"
                  absolute
                  right
                  top
                  fab
                  small
                >
                  x
                </v-btn>
                <TaskOverlay />
              </v-overlay>
            </v-row>
          </v-list-item-content>
        </v-list-item>
      </template>
    </v-list>
  </v-card>
</template>

<style scoped>
.no-flex {
  flex: auto !important;
}
</style>

<script>
import TaskOverlay from "./TaskOverlay.vue";
import api from "@/services/api";
export default {
  components: {
    TaskOverlay,
  },
  data: () => ({
    tasks: [],
    overlay: false,
    overlayDelete: false,
    zIndex: 10,
  }),

  mounted() {
    api.get("/tarefas").then((response) => {
      this.tasks = response.data;
    });
  },
  methods: {
    updateStatus(item){
      item.ativo = !item.ativo
      var data = {
        ativo: item.ativo
      };
      api.patch(`/tarefas/${item.id}/`, data).then((response) => {
        console.log(response)
      })
    },
    taskDelete(item){
      api.delete(`tarefas/${item.id}`).then(() => window.alert("deletado", document.location.reload()))
    }
  },
};
</script>
