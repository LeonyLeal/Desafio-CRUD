<template>
  <v-form
    ref="form"
    lazy-validation
    class="background"
  >
  <h2>Editar Tarefa</h2>
  <v-text-field
      v-model="TaskEdit.id"
      label="id"
      required
    ></v-text-field>
    <v-text-field
      v-model="TaskEdit.titulo"
      :counter="64"
      :rules="TaskEdit.tituloRules"
      label="Titulo"
      required
    ></v-text-field>

    <v-text-field
      v-model="TaskEdit.descricao"
      label="Descrição"
      required
    ></v-text-field>
    <v-select
      v-model="TaskEdit.contato_id"
      :items="contatos"
      item-text="nome"
      item-value="id"
      label="contatos"
      required
    ></v-select>
    <v-checkbox
      v-model="TaskEdit.ativo"
      label="ativo?"
      required
    ></v-checkbox>

    <v-btn
      :disabled="!validate"
      color="success"
      class="mr-4"
      @click="validate(TaskEdit)"
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
      TaskEdit:{
        id: 0,
        titulo:"",
        descricao:"",
        ativo:false,
        contato_id: "",
      },
      tituloRules:[ 
          v => !!v || 'Precisa de um titulo',
          v => (v && v.length <= 64) || 'titulo tem que ter menos de 64 caracteres',
        ],
      contatos: [],
    }),

    methods: {
      validate(item) {
        var data = {
          titulo: item.titulo,
          descricao: item.descricao,
          contato_id:item.contato_id,
          ativo: item.ativo,
        }
        console.log(data)
        api.patch(`/tarefas/${item.id}/`, data).then(response => {
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
  },
  }
</script>