<template>
  <v-form ref="form" lazy-validation class="background">
    <h2>Editar Tarefa</h2>
    <v-text-field
      v-model="TaskEdit.titulo"
      :counter="64"
      :rules="tituloRules"
      label="Titulo"
      required
    ></v-text-field>

    <v-text-field
      v-model="TaskEdit.descricao"
      :counter="128"
      :rules="descricaoRules"
      label="Descrição"
      required
    ></v-text-field>
    <v-select
      v-model="TaskEdit.contato_id"
      :rules="contatoRules"
      :items="contatos"
      item-text="nome"
      item-value="id"
      label="contatos"
      required
    ></v-select>
    <v-checkbox v-model="TaskEdit.ativo" label="ativo?" required></v-checkbox>

    <v-btn
      :disabled="!validate"
      color="success"
      class="mr-4"
      @click="validate(TaskEdit)"
    >
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
  props: ["task"],
  data: () => ({
    TaskEdit: {
      titulo: "",
      descricao: "",
      ativo: "",
      contato_id: 0,
    },
    tituloRules: [
      (v) => !!v || "O titulo é obrigatório",
      (v) =>
        (v && v.length <= 64) || "O titulo tem que ter menos de 64 caracteres",
    ],
    descricaoRules: [
      (v) => !!v || "Descrição é obrigatório",
      (v) =>
        (v && v.length <= 64) ||
        "A descrição tem que ter menos de 128 caracteres",
    ],
    contatoRules: [
      (v) => !!v || "E necessário atribuir essa tarefa a um contato",
    ],
    contatos: [],
  }),

  methods: {
    validate(item) {
      var data = {
        titulo: item.titulo,
        descricao: item.descricao,
        contato_id: item.contato_id,
        ativo: item.ativo,
      };
      console.log(data);
      api.patch(`/tarefas`, data).then((response) => {
        console.log(response);
        document.location.reload();
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
    console.log(this.task.id, "bbbb")
    api.get("/contatos").then((response) => {
      this.contatos = response.data;
    });
    //api.get(`/tarefas/${this.task.id}`).then((response) => {
    //  this.tasks = Object.keys(response.data);
    //  console.log(response.data, "aaa")
    //});
  },
};
</script>