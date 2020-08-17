<template>
  <div id="app">

      <form @submit.prevent="createMovie">
        <div class="form-group row">
          <input type="text" class="form-control col-3 mx-2" placeholder="id" v-model="movie.id">
          <input type="text" class="form-control col-3 mx-2" placeholder="title" v-model="movie.title">
          <input type="text" class="form-control col-3 mx-2" placeholder="genre" v-model="movie.genre">
          <button class="btn btn-success">Submit</button>
        </div>
      </form>

      <table class="table">
        <thead>
          <th>id</th>
          <th>title</th>
          <th>Genre</th>
        </thead>
        <tbody>
          <tr v-for="movie in movies" :key="movie.id">
            <td>{{ movie.id }}</td>
            <td>{{ movie.title }}</td>
            <td>{{ movie.genre }}</td>
          </tr>
        </tbody>
      </table>
  </div>
</template>

<script defer>

export default {
  name: 'App',
  data(){
    return {
      movie: {
        'id': '',
        'title': '',
        'genre': '',
      },
      movies: []
    }
  },

  async created(){
    var response = await fetch('http://localhost:8000/api/movies/');
      this.movies = await response.json();
  },

  methods: {
    async createStudent(){
      var response = await fetch('http://localhost:8000/api/movies/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.movie)
      });
      this.movies.push(await response.json());
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
