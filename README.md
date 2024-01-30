### Flask Ecommerce Application Design

**HTML Files:**

1. **index.html:**
   - Main landing page of the website.
   - Displays a list of available products and categories.
   - Provides a search bar for finding specific products.
   - Includes a shopping cart icon that leads to the cart page.

2. **product_details.html:**
   - Detailed page for each product.
   - Shows product images, descriptions, prices, and availability.
   - Offers options to add the product to the cart or add it to a wishlist.

3. **cart.html:**
   - Page for viewing and managing the shopping cart.
   - Lists the products added to the cart, along with their quantities and prices.
   - Provides a button for proceeding to checkout.

4. **checkout.html:**
   - Checkout page for completing the purchase.
   - Includes options for selecting a shipping address, payment method, and billing address.
   - Uses Stripe for processing payments securely.

**Routes:**

1. **Home Page (GET):**
   - Route for the main landing page of the website.
   - Displays the list of available products and categories.

2. **Product Details (GET):**
   - Route for the detailed page of a specific product.
   - Retrieves and displays product information from a database.

3. **Add to Cart (POST):**
   - Route for adding a product to the shopping cart.
   - Accepts a product ID and quantity as parameters and updates the cart accordingly.

4. **View Cart (GET):**
   - Route for displaying the shopping cart contents.

5. **Checkout (GET):**
   - Route for the checkout page.
   - Displays the cart contents and provides form fields for entering shipping and payment information.

6. **Process Checkout (POST):**
   - Route for processing the checkout request.
   - Validates the shipping and payment information and charges the customer using Stripe.

7. **Order Confirmation (GET):**
   - Route for displaying an order confirmation page after successful checkout.

8. **Wishlist (GET):**
   - Route for viewing and managing the wishlist.

9. **Add to Wishlist (POST):**
   - Route for adding a product to the wishlist.

10. **Remove from Wishlist (POST):**
   - Route for removing a product from the wishlist.