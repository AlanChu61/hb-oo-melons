"""Classes for melon orders."""

import random


class AbstractMelonOrder:
    """An abstract class for melon orders."""

    shipped = False

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.get_base_price()

    def get_base_price(self):
        """Calculate base price between 5 and 9 dollars.
        Multiply by 1.5 for Christmas Melons.
        """

        base_price = random.randint(5, 9)
        self.base_price = base_price
        if self.species == "christmas_melons":
            self.base_price = self.base_price * 1.5

    def get_total(self):
        """Calculate price, including tax.
        Example:
        self.tax = 5%
        self.base_price = 5
        order1 = DomesticMelonOrder("watermelon",8)
        total = (1+5%)*8* 5 = 42
        """
        total = (1 + self.tax) * self.qty * self.base_price
        print(f"Order details:")
        print(f"Order Type: {self.order_type}")
        print(f"Species: {self.species} ")
        print(f"Base Price: {self.base_price} ")
        print(f"QTY: {self.qty}")
        print(
            f"Subtotal: {self.base_price} * {self.qty} = {self.base_price * self.qty}")
        print(f"Tax: {self.tax}")
        print(f"Tax amt: {self.tax*self.base_price*self.qty}")
        print(f"Total: {total}")
        # return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    # def __init__(self, species, qty):
    #     super().__init__(species, qty)
    #     """Initialize melon order attributes."""


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""
        total = super().get_total()
        if self.qty < 10:
            flat_fee = 3
            # if self.species != "christmas_melons":
            #     base_price = 5
            # else:
            #     base_price = 5 * 1.5
            # base_price = 5.5 if self.species == "christmas_melons" else 5
            # total = ((1 + self.tax) * self.qty * self.base_price) + flat_fee
            return total + flat_fee
        else:
            return total

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        if passed == True:
            self.passed_inspection = True
