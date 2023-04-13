"""Classes for melon orders."""

# create AbstractMelonOrder


class AbstractMelonOrder:
    """An abstract class for melon orders."""
    shipped = False

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "christmas_melons":
            base_price = base_price * 1.5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08

    def __init__(self, species, qty):
        super().__init__(species, qty)
        """Initialize melon order attributes."""


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
        if self.qty < 10:
            """
            if self.speices == "christmas_melons"
                base_price = 5 *1.5
            else:
                base_price = 5
            """
            base_price = 5*1.5 if self.species == "christmas_melons" else 5
            total = ((1 + self.tax) * self.qty * base_price) + 3
            return total
        else:
            super().get_total()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
