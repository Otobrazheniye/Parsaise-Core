
import './styles/main.scss'

const app = document.querySelector('#app')

if (!app) {
  throw new Error('App root element not found')
}

app.innerHTML = `
  <header class="header">
    <a class="logo" href="#">
      PARADISE <span>CORE 89</span>
    </a>

    <nav aria-label="Main navigation">
      <a href="#about">About</a>
      <a href="#departments">Departments</a>
      <a href="#access">Access</a>
    </nav>
  </header>

  <main>
    <section class="hero" id="about">
      <div class="hero__content">
        <p class="eyebrow">PARADISE / CORE 89</p>
        <h1>
          A MODULAR<br />
          MANAGEMENT<br />
          <span>PLATFORM.</span>
        </h1>
        <p class="description">
          A unified entry point for independent
          departments, secure operations and
          coordinated business processes.
        </p>
        <a class="button" href="#departments">
          Explore platform
        </a>
      </div>
    </section>

    <section class="departments" id="departments">
      <h2>Initial departments</h2>

      <div class="department-grid">
        <article class="department-card">
          <span>01 / LOGISTICS</span>
          <h3>Logistics</h3>
          <p>Fleet, orders and shipments.</p>
        </article>

        <article class="department-card">
          <span>02 / MEDICAL</span>
          <h3>Medical</h3>
          <p>Patients, visits and scheduling.</p>
        </article>
      </div>
    </section>

    <section class="access" id="access">
      <h2>Authorized access</h2>
      <p>
        Registration and department access
        will be implemented in the authentication phase.
      </p>
    </section>
  </main>

  <footer class="footer">
    PARADISE CORE 89 / DEVELOPMENT BUILD
  </footer>
`
