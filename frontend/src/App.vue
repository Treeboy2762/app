<template>
  <div id="app">

      <form @submit.prevent="submitForm">
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
          <tr v-for="movie in movies" :key="movie.id" @dblclick="$data.movie = movie">
            <td>{{ movie.id }}</td>
            <td>{{ movie.title }}</td>
            <td>{{ movie.genre }}</td>
            <td>
              <button class="btn btn-outline-danger btn-sm ms-1" @click="deleteMovie(movie)">x</button>
            </td>
          </tr>
        </tbody>
      </table>
    <div v-show="is_show">
        <h5>뷰하!</h5>
        <p>v-if와 v-show로 모달창을 띄워봅시다.</p>
        <p>{{ placeholder }}</p>
        <button @click="handle_toggle" type="button">
            확인
        </button>
    </div>
  </div>
</template>

<script defer>

export default {
  name: 'App',
  data(){
    return {
      movie: {},
      movies: [],
      is_show: false,
      placeholder: '',
    }
  },

  async created(){
    await this.getMovies();
  },

  methods: {

    handle_toggle: function(text){ 
      this.is_show = !this.is_show; // #2, #3
      this.placeholder = text;
    },

    submitForm(){
      if (this.movie.id === undefined) {
        this.createMovie();
      }

      else {
        this.editMovie();
      }
        
    },

    async getMovies() {
      var response = await fetch('http://localhost:8000/api/movies/');
      this.movies = await response.json();
    },

    async createMovie(){
      await this.getMovies

      await fetch('http://localhost:8000/api/movies/', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.movie)
      });
      await this.getMovies();
    },

    async editMovie(){
      await this.getMovies

      await fetch(`http://localhost:8000/api/movies/${this.movie.id}/`, {
        method: 'put',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.movie)
      });
      await this.getMovies();
      this.movie = {}
    },

    async deleteMovie(movie){
      await this.getMovies

      await fetch(`http://localhost:8000/api/movies/${movie.id}/`, {
        method: 'delete',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.movie)
      });
      await this.getMovies();
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
