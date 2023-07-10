import React, { useState, useEffect } from 'react';
import {
  BrowserRouter,
  Route,
  Routes,
  Link,
  useParams
} from "react-router-dom";

/*
  1. get react router working (route to book component that displays isbn)
  2. get api call working
  3. grab data we want from api call
  4. style book component and add book info from api call
*/

function Book() {
  let [bookInfo, setBookInfo] = useState({})

  let { isbn } = useParams();

  const fetchData = async () => {
    const data = await fetch(`https://openlibrary.org/isbn/${isbn}.json`);
    const fetched = await data.json();
    setBookInfo(fetched)
  }

  useEffect(() => {
    fetchData();
  }, []);
    

  return (
    <div className="book-info">
      <div>
        <h2>{bookInfo.title}</h2>
        <p>ISBN: {bookInfo.isbn_13}</p>
        <p>Published: {bookInfo.publish_date}</p>
        <p>Pages: {bookInfo.number_of_pages}</p>
        {/* need to add mapping over multiple publishers (ex: https://fzr6gpwh.cdpad.io/9780618002214) */}
        <p>Publishers: {bookInfo.publishers}</p>
      </div>
      <img src="https://images.unsplash.com/photo-1688989680825-0790dc6488fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80" width="200px" height="200px" alt="hello" class="photo" />
    </div> 
    
  )
}

// https://openlibrary.org/isbn/9780140328721.json

function Home() {
  return (
    <div>
      Enter https://fzr6gpwh.cdpad.io/isbn to display book info for that isbn
    </div>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route index element={<Home />} />
        <Route path="/:isbn" element={<Book />} />
      </Routes>
    </BrowserRouter>
  );
}
