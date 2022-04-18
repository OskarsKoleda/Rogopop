<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <router-link class="navbar-brand" :to="{ name: 'home' }"
        >&#9760;Rogopop App&#9760;</router-link
      >
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarTogglerDemo02"
        aria-controls="navbarTogglerDemo02"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav ms-auto mt-2 mt-lg-0">
          <li class="nav-item active me-3">
            <a class="btn btn-success" href="/">Books</a>
          </li>
          <li class="nav-item active me-3">
            <router-link class="btn btn-success" :to="{ name: 'concerts', params: {page: 1} }"
              >Events</router-link
            >
          </li>
          <li class="nav-item active me-3">
            <router-link class="btn btn-success" :to="{ name: 'profile' }"
              >Profile</router-link
            >
          </li>
          <li class="nav-item active">
            <a class="btn btn-outline-secondary" href="/accounts/logout/"
              >Logout</a
            >
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {};
</script>

<style scoped>
.navbar {
  background-color: #d8d1c6 !important;
}
.my-navbar {
  border-bottom: 1px solid #ddd;
}
.navbar-brand {
  font-weight: bold;
  font-size: 150%;
}

.navbar-brand:hover {
  color: #dc3545;
}
</style>
