const Produce = ({ products, setProducts }) => {
  

  function clickedAddProduce(index){
    const updatedProducts = { ... products[index], qty: products[index].qty + 1 }
    const newProducts = [...products];
    newProducts[index] = updatedProducts;
    setProducts(newProducts);
  }
  
    return (
    <>
      {products.map((product, index) => (
      <p>{product.name} ${product.price} {product.qty}  
        <button onClick={()=>{clickedAddProduce(index)}}>+</button> 
      </p>
    ))}

    </>
  )
}

export default Produce;