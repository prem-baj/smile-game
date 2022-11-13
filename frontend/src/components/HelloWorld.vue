<template>
  <v-container>
    <v-row justify="center" align="center" class="text-center">
        <p class="mt-10" v-if="loading">
          Loading your quizz
        </p>
        <v-row v-else>

          <v-col cols="12">
            <v-img
              contain
              class="px-10"
              alt="quiz-img"
              :src="imageSrc"
              width="100%"
            />
          </v-col>
          <v-col cols="12">
            <v-row class="text-center">
              <v-col>
                <v-btn large width="100%">
                {{answers[0]}}
                </v-btn>
              </v-col>
              <v-col>
                <v-btn large width="100%">
                {{answers[1]}}
                </v-btn>
              </v-col>
            </v-row>
            <v-row class="text-center">
              <v-col>
                <v-btn large width="100%">
                {{answers[2]}}
                </v-btn>
              </v-col>
              <v-col>
                <v-btn large width="100%">
                {{answers[3]}}
                </v-btn>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-row>
  </v-container>
</template>

<script>
  import axios from 'axios';
  export default {
    name: 'HelloWorld',

    data: () => ({
      imageSrc: "",
      loading: true,
    }),
    methods: {
    async setQuiz() {
      this.loading = true;
      const res = await axios.get("http://localhost:5000/get_quiz");
      this.loading = false;
      console.log(res.data);
      this.imageSrc = res.data.question;
      this.answers = res.data.answers;
    }
  },
  created() {
    this.setQuiz()
  }
  }
</script>
