// import logo from './logo.svg';
import { useEffect, useState } from "react"; // React hooks for state and side effects
import './App.css'; // Import CSS styles
import HandleNewProductForm from "./form";

function App() {
  const [data, setData] = useState(null); // State to store data fetched from the backend

  const fetchData = () => {
    fetch("/data")
      .then(res => res.json()) // Convert the response to JSON
      .then(json => setData(json.DBResult)) // Save the result into state
      .catch(err => console.error("Error fetching data:", err)); // Handle errors
  };

  // useEffect runs after the component is mounted
  useEffect(() => {
    // Fetch data from backend route /data
    fetchData();
  }, []);

  // While data is still null, show "Loading..."
  if (!data) return <p>Loading...</p>;

  // Once data is available, render it as a table
  return (
    <div>
      <h1>Productes</h1>
      <HandleNewProductForm refetch={fetchData} />
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nom</th>
            <th>Nutri Score</th>
            <th>Nova Score</th>
            <th>Green Score</th>
          </tr>
        </thead>
        <tbody>
          {data.map((row, i) => (
            <tr key={i}>
              <td>{row[0]}</td>
              <td>{row[1]}</td>
              <td>{row[2]}</td>
              <td>{row[3]}</td>
              <td>{row[4]}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App; // Export App so it can be used in index.js
