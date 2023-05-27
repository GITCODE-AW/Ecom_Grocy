function add_to_cart(product_id) {
    let flag = 0
    let cart = JSON.parse(localStorage.getItem('cart'))
    
    if (cart) {
        if (cart[`${product_id}`]){
            cart[`${product_id}`]++
            localStorage.setItem('cart', JSON.stringify(cart))

        }
        else{
            cart[`${product_id}`] = 1
            localStorage.setItem('cart', JSON.stringify(cart))

        }
    } else {
        let new_cart = {}
        new_cart[`${product_id}`] = 1
        localStorage.setItem('cart', JSON.stringify(new_cart))
    }
    flag = 0
};