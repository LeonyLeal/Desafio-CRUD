<template>
  <v-form ref="form" lazy-validation class="background">
    <h2>Criar uma nova tarefa</h2>
    <v-text-field
      v-model="NewContact.nome"
      :counter="64"
      :rules="nomeRules"
      label="nome"
      required
    ></v-text-field>

    <v-text-field
      v-model="NewContact.email"
      label="Email"
      :rules="emailRules"
      required
    ></v-text-field>
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
    NewContact: {
      nome: "",
      email: "",
    },
    nomeRules: [
      (v) => !!v || "é necessário um nome",
      (v) => (v && v.length <= 64) || "nome tem que ter menos de 64 caracteres",
    ],
    emailRules: [
      (v) => !!v || "é necessário um Email",
    ],
    contatos: [],
  }),

  methods: {
    validate() {
      var data = this.NewContact;
      console.log(data); // Para me mostrar os dados antes de enviar caso um erro ocorra e já analisar o que foi de fato enviado
      api.post("/contatos/", data).then((response) => {
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
    api.get("/contatos").then((response) => {
      this.contatos = response.data;
    });
  },
};
</script>