import { useState } from "react";
import Produce from "./Produce"
import './App.css'
import ShoppingCart from './ShoppingCart'

export default function App() {
  const [products, setProducts] = useState([
    {name: 'Banana', price: 0.5, qty: 0},
    {name: 'Zucchini', price: 2.99, qty: 0},
    {name: 'Red Bell Pepper', price: 2.69, qty: 0},
    {name: 'Broccoli', price: 2.99, qty: 0},
    {name: 'Bluebberies', price: 4.49, qty: 0}  
  ]);
  
  return (
    <main>
      <Produce products={products} setProducts={setProducts} />
      <ShoppingCart products={products} setProducts={setProducts}/>
    </main>
  )
}
