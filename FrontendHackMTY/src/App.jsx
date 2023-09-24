import { useState, useRef, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios';

function App() {
  const [input, setInput] = useState({first: "", last: ""})
  const [server, setServer] = useState("")
  const [text, setText] = useState("")
  const [pos, setPos] = useState({x: 0, y: 0})
  let i = useRef(0)

  useEffect(() => {
    fetch("http://127.0.0.1:5000/get_data").then(res => res.json()).then(data => setServer(data))
  }, [])
  console.log(server)
  const handleFormSubmit = async (event) => {
    event.preventDefault();

    try {
      // Save data to Local Storage
      localStorage.setItem('user_data', input.first,input.last);

      // Send data to Flask backend using Axios
      const response = await axios.post('http://127.0.0.1:5000/insert_data', {
        data: input.first,
        last: input.last,
      });

      console.log(response.data);
      console.log(response.last);
      // You can perform additional actions based on the Axios response
    } catch (error) {
      console.error(error);
    }

    console.log(input.first, input.last);
  };
  return (
    <>
      {/* <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p> */}
      <h1>{text}</h1>
      <button onClick={(event) => {
        i.current++
        if (i.current < 5) setPos({x: (Math.random() * 250) + 15, y: (Math.random() * 250) + 15})
        else setText(prevText => prevText != "Hola mundo" ? "Hola mundo" : "Que guapo Azahel 🎅")
      }} style={
        {transform: `translate(${pos.x}px, ${pos.y}px)`}
      }>Click Me!</button>
      <form>
        <label htmlFor='first'>First name:</label>
        <input type="text" placeholder='Peter' id="first" value={input.first} onChange={(event) => {setInput(prevInput => ({first: event.target.value, last: prevInput.last}))}}/>
        <label htmlFor='last'>Last name:</label>
        <input type="text" placeholder='Parker' id="last" value={input.last} onChange={(event) => {setInput(prevInput => ({first: prevInput.first, last: event.target.value}))}}/>
        <button type="submit" onClick={handleFormSubmit}>Submit</button>
      </form>
    </>
  )
}

export default App
