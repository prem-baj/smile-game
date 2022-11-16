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
                <v-btn
                  large width="100%"
                  :loading="submiting" 
                  :color="selectedAnswerNum == 0 ? answeredCorrect ? 'green' : 'red': ''"
                  @click="!(submiting || answered) && submitSolution(0)"
                >
                {{answers[0]}}
                </v-btn>
              </v-col>
              <v-col>
                <v-btn 
                  large width="100%"
                  :loading="submiting" 
                  :color="selectedAnswerNum == 1 ? answeredCorrect ? 'green' : 'red': ''"
                  @click="!(submiting || answered) && submitSolution(1)"
                >
                {{answers[1]}}
                </v-btn>
              </v-col>
            </v-row>
            <v-row class="text-center">
              <v-col>
                <v-btn 
                  large width="100%"
                  :loading="submiting" 
                  :color="selectedAnswerNum == 2 ? answeredCorrect ? 'green' : 'red': ''"
                  @click="!(submiting || answered) && submitSolution(2)"
                >
                {{answers[2]}}
                </v-btn>
              </v-col>
              <v-col>
                <v-btn 
                  large width="100%"
                  :loading="submiting" 
                  :color="selectedAnswerNum == 3 ? answeredCorrect ? 'green' : 'red': ''"
                  @click="!(submiting || answered) && submitSolution(3)"
                >
                {{answers[3]}}
                </v-btn>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="12">
            <v-btn 
              v-if="answered"
              large width="200px"
              @click="setQuiz()"
            >
              NEXT
            </v-btn>
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
      submiting: false,
      answers: [],
      answered: false,
      answeredCorrect: false,
      selectedAnswerNum: null,
    }),
    methods: {
    async setQuiz() {
      this.answered = false;
      this.answeredCorrect = false
      this.selectedAnswerNum = null;
      this.loading = true;
      const res = await axios.get("http://localhost:5000/quiz");
      this.loading = false;
      console.log(res.data);
      this.imageSrc = res.data.question;
      this.answers = res.data.answers;
    },
    async submitSolution(num) {
      this.selectedAnswerNum = num
      const solution = this.answers[num]
      this.submiting = true;
      const res = await axios.post(`http://localhost:5000/quiz/answer/${solution}`);
      this.submiting = false;
      console.log(res.data);
      this.answered = true;
      this.answeredCorrect = res.data.correct
    }
  },
  created() {
    this.setQuiz()
  }
  }
</script>
