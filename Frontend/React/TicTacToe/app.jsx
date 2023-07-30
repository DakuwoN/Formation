import React from 'react';

// class Greeting extends PureComponent {
//   render() {
//     return <h1>Hello, {this.props.name}!</h1>;
//   }
// }
class App extends React.Component {

  render () {
    return (
      <Board/>
    )
  }
}

/*
class Counter extends Component {
  state = {
    age: 42,
  };

  handleAgeChange = () => {
    this.setState({
      age: this.state.age + 1 
    });
  };

  render() {
    return (
      <>
        <button onClick={this.handleAgeChange}>
        Increment age
        </button>
        <p>You are {this.state.age}.</p>
      </>
    );
  }
}

Check if the box is empty. If the box is empty, we can fill the box with an 
X, and at the same time we need to fill another box with an O.
Once the user clicks--we need to fill two boxes, one with an X and one with an O.
If the user clicks an index on the board that's occupied--we do nothing. 
*/

class Board extends React.Component {
  state = {
    board:  Array(9).fill(null),
    currPlayer: 'x'
  }

  handleClick = (index) => {
    const {board, currPlayer} = this.state;
    if (board[index]) return;
    
    const newBoard = [...board]
    newBoard[index] = 'x'
    
    // check if user won

    if (newBoard.every(ele => ele !== null)) return;

    // AI makes a move
    let randIdx = Math.floor(Math.random() * 9)
    while (newBoard[randIdx]) {
      randIdx = Math.floor(Math.random() * 9)
    }
    newBoard[randIdx] = 'o'
    this.setState({
      board: newBoard,
    })
  }

  render () {
    
    return(
      <div className="board">
        {this.state.board.map((value, index) => <Cell handleClick={() => this.handleClick(index)} key={index} value={value}/>)}
      </div>
    )
  }
}



class Cell extends React.Component {
  render () {
    const { value, handleClick } = this.props;
    return (
    <div className='cell' onClick={handleClick}>{value}</div>
  )}
}



export default App;