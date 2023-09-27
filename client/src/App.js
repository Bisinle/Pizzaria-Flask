import { Routes, Route } from "react-router-dom";
import "./App.css";
import Navbar from "./components/Navbar";
import Pizzas from "./components/Pizzas";
import About from "./components/Rest";
import Contacts from "./components/Contacts";

import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("https://pizzaria-kk81.onrender.com//pizzas")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);
  console.log(data);
  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="about" element={<Rest />} />
        <Route path="/pizzas" element={<Pizzas restaurants={data} />} />
        {/* <Route path="contact" element={<Contacts />} /> */}
      </Routes>
    </div>
  );
}

export default App;
