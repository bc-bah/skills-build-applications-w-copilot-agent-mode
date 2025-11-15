import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <nav className="navbar navbar-expand-lg navbar-light bg-light mb-4">
        <div className="container-fluid">
          <a className="navbar-brand" href="/">OctoFit Tracker</a>
          <div className="collapse navbar-collapse">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item"><a className="nav-link" href="/activities">Activities</a></li>
              <li className="nav-item"><a className="nav-link" href="/leaderboard">Leaderboard</a></li>
              <li className="nav-item"><a className="nav-link" href="/teams">Teams</a></li>
              <li className="nav-item"><a className="nav-link" href="/users">Users</a></li>
              <li className="nav-item"><a className="nav-link" href="/workouts">Workouts</a></li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container">
        <h2>Welcome to OctoFit Tracker!</h2>
        <p>Track your fitness, join teams, and compete on the leaderboard.</p>
      </div>
    </div>
  );
}

export default App;
