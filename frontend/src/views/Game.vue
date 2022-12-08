<template>
  <v-container>
    <v-row justify="center" align="center" class="text-center">
        <p class="mt-10" v-if="loading">
          Loading your quizz
        </p>
        <v-row v-else>
          <p>Correct answers: {{correctCount}}</p>
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
  import UserService from '../services/user.service'
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
      correctCount: 0
    }),
    methods: {
    async setQuiz() {
      this.answered = false;
      this.answeredCorrect = false
      this.selectedAnswerNum = null;
      this.loading = true;
      const res = await await UserService.getQuiz()
      this.loading = false;
      console.log(res.data);
      this.imageSrc = res.data.question;
      this.answers = res.data.answers;
      this.correctCount = res.data.correct_count;
    },
    async submitSolution(num) {
      this.selectedAnswerNum = num
      const solution = this.answers[num]
      this.submiting = true;
      // const res = await axios.post(`http://localhost:5000/quiz/answer/${solution}`);
      const res = await UserService.submitSolution(solution)
      this.submiting = false;
      this.answered = true;
      this.answeredCorrect = res.data.correct
    }
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  watch: {
    loggedIn(val) {
      if (!val) {
            this.$router.push('/login');
      }
    }
  },
  created() {
    if (!this.loggedIn) {
      this.$router.push('/login');
    }
    this.setQuiz()
  }
  }
</script>
