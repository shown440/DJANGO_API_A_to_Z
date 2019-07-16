import React, { Component } from 'react';
import axios from 'axios';


const QUOTES_API = 'http://127.0.0.1:8000/api/quotes/?format=json';

class App extends Component{

  state = {
    quotes: []
  }

  componentDidMount(){
    this.getCategories()
  }

  // Loading data from remote end points
  getCategories(){
    axios.get(QUOTES_API)
    .then(res => {
      console.log(res.data);
      this.setState({quotes: res.data})
    })
    .catch(err => {
      console.log(err)
    })
  }

  render(){
    return(
      <div>
        {this.state.quotes.map(item => (
          <div>
            <p>{ item.quote }</p>
            <p><strong>{ item.author }</strong></p>
          </div>
        ))}
      </div>
    )
  }

}
export default App;




/////////////////////////////////////////////////////////////////////////////
//  Default Codes
////////////////////////////////////////////////////////////////////////////

// import React from 'react';
// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
