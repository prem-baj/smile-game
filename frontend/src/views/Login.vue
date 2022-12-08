<template>
  <v-form ref="form" lazy-validation>
    <h1>Login</h1>
    <v-text-field v-model="user.username" label="Username" required></v-text-field>

    <v-text-field
      v-model="user.password"
      label="Password"
      type="password"
      required
    ></v-text-field>

    <v-btn
      :disabled="!user.username || !user.password"
      color="success"
      class="mr-4"
      @click="handleLogin"
    >
      Submit
    </v-btn>
  </v-form>
</template>

<script>
import User from "../models/user";

export default {
  name: "Login",
  data() {
    return {
      user: new User("", ""),
      loading: false,
      message: "",
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    },
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/');
    }
  },
  methods: {
    handleLogin() {
      this.loading = true;

      if (this.user.username && this.user.password) {
        this.$store.dispatch("auth/login", this.user).then(() => {
            this.$router.push('/');
        });
      }
    },
  },
};
</script>
