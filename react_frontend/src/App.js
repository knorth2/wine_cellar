import React, { useState, useEffect } from 'react'
import {Route, Routes, useNavigate} from 'react-router-dom'
import './App.css';
import Home from './Screens/Home'

function App() {
  return (
    <div className="App">
      <h1>Wine Cellar</h1>
      <Routes>
      <Route path='home' element={<Home/>}/>
      </Routes>
    </div>
  );
}

export default App;
