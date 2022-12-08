import axios from 'axios';
import authHeader from './auth-header';

class UserService {
  getQuiz() {
    return axios.get(`http://localhost:5000/quiz`, { headers: authHeader() });
  }

  submitSolution(solution) {
    return axios.post(`http://localhost:5000/quiz/answer/${solution}`, {}, { headers: authHeader() });
  }
}

export default new UserService();