import axios from 'axios';

class AuthService {
  login(user) {
    return axios
      .post('http://localhost:5000/login', {
        username: user.username,
        password: user.password
      })
      .then(response => {
        console.log("LOGING ",response.data)
        if (response.data.token) {
          localStorage.setItem('user', JSON.stringify(response.data));
        }

        return response.data;
      });
  }

  logout() {
    localStorage.removeItem('user');
  }

  register(user) {
    return axios.post('http://localhost:5000/register', {
      username: user.username,
      password: user.password,
    });
  }
}

export default new AuthService();