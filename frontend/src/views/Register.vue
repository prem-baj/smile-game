<template>
  
  <v-form
    ref="form"
  >
    <h1>Register</h1>
    <v-text-field
      v-model="user.username"
      label="Username"
      required
    ></v-text-field>

    <v-text-field
      v-model="user.password"
      label="Password"
      type="password"
      required
    ></v-text-field>

     <v-text-field
      v-model="repeatPassword"
      label="Repeat password"
      type="password"
      required
    ></v-text-field>

    <v-btn
      :disabled="!user.password || user.password != repeatPassword"
      color="success"
      class="mr-4"
      @click="handleRegister"
    >
      Submit
    </v-btn>
    <div v-if="message">
        {{message}}
    </div>
  </v-form>

</template>

<script>
import User from '../models/user';

export default {
  name: 'Register',
  data() {
      return {
      user: new User('', '', ''),
      submitted: false,
      successful: false,
      message: '',
      repeatPassword: ''
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  mounted() {
    if (this.loggedIn) {
      this.$router.push('/profile');
    }
  },
  methods: {
    handleRegister() {
      this.message = '';
      this.submitted = true;
    //   this.$validator.validate().then(isValid => {
    //     if (isValid) {
    this.$store.dispatch('auth/register', this.user).then(
        data => {
            this.message = data.message;
            this.successful = true;
        },
        // error => {
        //   this.message =
        //     (error.response && error.response.data) ||
        //     error.message ||
        //     error.toString();
        //   this.successful = false;
        // }
    );
    //     }
    //   });
    }
  }
};
</script>