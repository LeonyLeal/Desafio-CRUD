<template>
  <v-form ref="form" lazy-validation class="background">
    <h2>Criar uma nova tarefa</h2>
    <v-text-field
      v-model="NewTask.titulo"
      :counter="64"
      :rules="tituloRules"
      label="Titulo"
      required
    ></v-text-field>

    <v-text-field
      v-model="NewTask.descricao"
      label="Descrição"
      :counter="128"
      :rules="descricaoRules"
      required
    ></v-text-field>
    <v-select
      v-model="NewTask.contato_id"
      :items="contatos"
      :rules="contatoRules"
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
      titulo: "",
      descricao: "",
      ativo: true,
      contato_id: "",
    },
    tituloRules: [
      (v) => !!v || "O titulo é obrigatório",
      (v) =>
        (v && v.length <= 64) || "O titulo tem que ter menos de 64 caracteres",
    ],
     descricaoRules: [
      (v) => !!v || "Descrição é obrigatório",
      (v) =>
        (v && v.length <= 64) || "A descrição tem que ter menos de 128 caracteres",
    ],
    contatoRules: [
      (v) => !!v || "E necessário atribuir essa tarefa a um contato",
    ],
    contatos: [],
  }),
  methods: {
    validate() {
      var data = this.NewTask;
      console.log(data);
      api.post("/tarefas/", data).then((response) => {
        console.log(response);
        window.location.reload();
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
  },
};
</script>