  
import React from 'react';

import './App.css';
import Dropzone from "./dropzone/Dropzone";

function App() {
  return (
    <div className="background">
      <p className="title">Image Processing Microservice</p>
      <div className="content">
        <Dropzone />
      </div>
    </div>
  );
}

export default App;