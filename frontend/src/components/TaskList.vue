<template>
  <v-card max-width="450" class="mx-auto">
    <template v-for="task in tasks">
      <v-list three-line id="o que isso" :key="task.id">
        <v-list-item :id="task.id">
          <v-col class="flex-grow-0 pa-0 pr-10 text-center">
            <p class="" v-html="task.contato_id"></p>
          </v-col>
          <v-list-item-content>
            <v-row class="ma-0">
              <v-list-item-title class="no-flex"
                ><strong
                  >{{ task.titulo }}</strong
                ></v-list-item-title
              >
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
              <v-btn elevation="2" raised @click="overlayEdit = !overlayEdit">
                Editar{{task.id}}</v-btn
              >
              <v-btn
                elevation="2"
                raised
                color="error"
                :key="task.id"
                @click="taskDelete(task)"
              >
                Deletar{{task.id}}</v-btn
              >
              <v-overlay :z-index="zIndex" :value="overlayEdit">
                <v-btn
                  class="white--text"
                  color="error"
                  @click="overlayEdit = false"
                  absolute
                  right
                  top
                  fab
                  small
                >
                  x
                </v-btn>
                <TaskOverlay :task="tasks"/>
              </v-overlay>
            </v-row>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </template>
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
    overlayEdit: false,
    zIndex: 100,
  }),
  methods: {
    updateStatus(item) {
      //Atualizar Ativo no banco de dados
      item.ativo = !item.ativo;
      var data = {
        ativo: item.ativo,
      };
      api.patch(`/tarefas/${item.id}/`, data).then((response) => {
        console.log(response);
      });
    },
    taskDelete(item) {
      api.delete(`tarefas/${item.id}`).then(() => window.location.reload());
    },
  },
  mounted() {
    api.get("/tarefas").then((response) => {
      this.tasks = response.data;
    });
  },
};
</script>
