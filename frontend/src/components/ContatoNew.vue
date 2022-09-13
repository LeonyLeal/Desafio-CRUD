<template>
  <v-form
    ref="form"
    lazy-validation
    class="background"
  >
  <h2>Criar uma nova tarefa</h2>
  <p>Proximo id é {{TotalId+1}}</p>
  <v-text-field
      v-model="NewTask.id"
      label="id"
      required
    ></v-text-field>
    <v-text-field
      v-model="NewTask.nome"
      :counter="64"
      :rules="NewTask.nomeRules"
      label="nome"
      required
    ></v-text-field>

    <v-text-field
      v-model="NewTask.email"
      label="Email"
      required
    ></v-text-field>
    <v-btn
      :disabled="!validate"
      color="success"
      class="mr-4"
      @click="validate"
    >
      validar
    </v-btn>

    <v-btn
      color="error"
      class="mr-4"
      @click="reset"
    >
      Resetar
    </v-btn>

    <v-btn
      color="warning"
      @click="resetValidation"
    >
      Revalidar
    </v-btn>
  </v-form>
</template>

<style scoped>
.background{
    padding: 20px;
    border-radius: 10px;
    background-color: #303030;
}
</style>

<script>
import api from '@/services/api'
  export default {
    data: () => ({
      NewTask:{
        id: 0,
        nome:"",
        email:"",
        ativo:false,
        contato_id: "",
      },
      TotalId: 0 ,
      nomeRules:[ 
          v => !!v || 'Precisa de um nome',
          v => (v && v.length <= 64) || 'nome tem que ter menos de 64 caracteres',
        ],
      contatos: [],
    }),

    methods: {
      validate () {
        var data = this.NewTask;
        console.log(data)
        api.post('/contatos/', data).then(response => {
          console.log(response)
          document.location.reload()
        })
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    },
     mounted() {
   api.get("/contatos").then((response) => {
      this.contatos = response.data
    });
    api.get("/contatos").then((response) =>{ 
        console.log(Object.keys(response.data).length)
        this.TotalId = Object.keys(response.data).length})
  },
  }
</script>