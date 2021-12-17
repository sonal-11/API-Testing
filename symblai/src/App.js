import classes from './App.module.css';
import React, { useEffect, useState } from "react";
// import Header from "./components/Header";

function App() {
  const [data, setData] = useState();

  useEffect(() => {
    fetch("http://127.0.0.1:5000/data")
      .then(response => {
          return response.json();
      })
      .then((res) => {
        setData(res);
        console.log(res)
      })
      .catch((error) => {
        console.log(error);
      })
  }, []);

  let Component = null;

  if (data) {
    Component = Object.keys(data).map((Data) => {

    const id_data = data[Data].id;
    const name_data = data[Data].item;

    console.log(id_data);
    console.log(name_data);
    
      
      return (
        <div key={Data}>
          <div className={classes.Abcd}>
            This keys are printed as: {Object.values(id_data).map(i => <p>{i}</p>)}
            This are names: {Object.values(name_data).map(i => <p>{i}</p>)}
          </div>
        </div>
      );
    });
  }

  return <div className="App">{Component}</div>;
}

export default App;