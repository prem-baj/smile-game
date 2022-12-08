<template>
  <v-app>
    <v-toolbar>
      <v-toolbar-title>Smile Game</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-menu v-if="currentUser" offset-y>
        <template v-slot:activator="{ attrs, on }">
          <v-btn color="green" class="white--text ma-5" v-bind="attrs" v-on="on">
            {{ currentUser.username }}
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="item in loggedOptions"
            :key="item.id"
            link
            @click="item.onClick"
          >
            <v-list-item-title v-text="item.text"></v-list-item-title>
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list>
      </v-menu>
      <div v-else>
        <v-btn color="green" class="white--text" @click="$router.push('/register')">
          Register
        </v-btn>
        <v-btn color="green" class="white--text mx-2" @click="$router.push('/login')">
          Login
        </v-btn>
      </div>
    </v-toolbar>

    <v-main>
      <!-- Provides the application the proper gutter -->
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "app",
  data() {
    return {
      loggedOptions: [
        {
          id: "log-out",
          text: "Log out",
          icon: "mdi-exit-to-app",
          onClick: () => this.$store.dispatch("auth/logout"),
        },
      ],
    };
  },
  computed: {
    currentUser() {
      return this.$store.state.auth.user;
    },
  },
  methods: {
    logOut() {
      this.$store.dispatch("auth/logout");
      this.$router.push("/login");
    },
  },
};
</script>
