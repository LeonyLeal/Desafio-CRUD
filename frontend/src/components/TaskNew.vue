<template>
  <v-form ref="form" lazy-validation class="background">
    <h2>Criar uma nova tarefa</h2>
     <p>Proximo id é {{TotalId+1}}</p>
    <v-text-field v-model="NewTask.id" label="id" required></v-text-field>
    <v-text-field
      v-model="NewTask.titulo"
      :counter="64"
      :rules="NewTask.tituloRules"
      label="Titulo"
      required
    ></v-text-field>

    <v-text-field
      v-model="NewTask.descricao"
      label="Descrição"
      required
    ></v-text-field>
    <v-select
      v-model="NewTask.contato_id"
      :items="contatos"
      item-text="nome"
      item-value="id"
      label="contatos"
      required
    ></v-select>
    <v-checkbox v-model="NewTask.ativo" label="ativo?" required></v-checkbox>

    <v-btn :disabled="!validate" color="success" class="mr-4" @click="validate">
      validar
    </v-btn>

    <v-btn color="error" class="mr-4" @click="reset"> Resetar </v-btn>

    <v-btn color="warning" @click="resetValidation"> Revalidar </v-btn>
  </v-form>
</template>

<style scoped>
.background {
  padding: 20px;
  border-radius: 10px;
  background-color: #303030;
}
</style>

<script>
import api from "@/services/api";
export default {
  data: () => ({
    NewTask: {
      id: 0,
      titulo: "",
      descricao: "",
      ativo: false,
      contato_id: "",
    },
    TotalId: 0 ,
    tituloRules: [
      (v) => !!v || "Precisa de um titulo",
      (v) =>
        (v && v.length <= 64) || "titulo tem que ter menos de 64 caracteres",
    ],
    contatos: [],
  }),

  methods: {
    validate() {
      var data = this.NewTask;
      console.log(data);
      api.post("/tarefas/", data).then((response) => {
        console.log(response);
      });
        api.get("/tarefas").then((response) => {
      this.tasks = response.data;
      document.location.reload()
    });
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
  mounted() {
    api.get("/contatos").then((response) => {
      this.contatos = response.data;
    });
     api.get("/tarefas").then((response) =>{ 
        console.log(Object.keys(response.data).length)
        this.TotalId = Object.keys(response.data).length})
  },
  
};
</script>