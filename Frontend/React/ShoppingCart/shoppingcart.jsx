const ShoppingCart = ({products, setProducts}) =>{

  function getTotal () {
    let total = 0;
    for(let product of products) {
      total += (product.qty * product.price)
    }
    
    return total.toFixed(2);
  }

  function removeProduct(index) {
    const updatedProducts = { ... products[index], qty: 0 }
    const newProducts = [...products];
    newProducts[index] = updatedProducts;
    setProducts(newProducts);
  }
  
  return (
    <>
      <h1>Shopping Cart</h1>
       {products.filter(product => product.qty >= 1).map((product, index) => (
      <p>{product.name} ${product.price} {product.qty}  
        <button onClick={()=>{removeProduct(index)}}>x</button> 
      </p>
    ))}
      <h2>Total: ${getTotal()} </h2>
    </>
  );
}


export default ShoppingCart;