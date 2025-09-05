def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount.
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage
    Returns:
    float:Final price after discount (if applicable) or original price"""

    if discount_percent >= 20:
        discount_amount = price * (discount_percent/100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
def main():
    """Main function to interact with the user and calculate discounts"""
    print("===Discount Calculator===")
    print("Discounts are applied only if 20% or higher")
    print("-" * 30)

    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percent = float(input("Enter the discout percentage:"))
        final_price = calculate_discount(original_price, discount_percent)

        print("\n" + "=" * 30)
        if discount_percent >= 20:
            print(f"Original Price: ${original_price:.2f}")
            print(f"Discount: {discount_percent}%")
            print(f"Discount Amount: ${(original_price * discount_percent / 100):.2f}")
            print(f"Final Price: ${final_price:.2f}")
            print(f"You saved:${(original_price - final_price):.2f}")
        else:
            print(f"Discount ({discount_percent}%) is less than 20%")
            print(f"No discount applied. Price remains: ${final_price:2.f}")
        print("=" * 30)

    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occured: {e}")
if __name__ == "__main__":
    main()