class Stock:

    # Name, the highest price, the lowest price, highest date, lowest date, beta, solidity, p/e, p/s
    def __init__(self, name, hi_price, lo_price, hi_date, lo_date, beta, growth, solidity, pe, ps):
        self.name = name  # String, name of stock
        self.beta = beta  # Float, latest price / oldest price
        self.growth = growth

        self.solidity = solidity  # Int - fundamenta.txt
        self.pe = pe  # String - fundamenta.txt
        self.ps = ps  # Float- fundamenta.txt

        self.hi_price = hi_price  # Float - the highest price
        self.lo_price = lo_price  # Float - the lowest price
        self.hi_date = hi_date
        self.lo_date = lo_date

    def __self__(self):
        return print(self.name)

    def fundamental_analysis(self):
        return print("Fundamental Analysis for " + self.name + "\n"
                     "—————————————————————————————————\n"
                     "Company solidity is " + self.solidity + "%\n" +
                     "Company p/e-number is " + self.pe +
                     "\nCompany p/s- number is " + self.ps)

    def technical_analysis(self):
        return print("Technical Analysis for " + self.name + "\n"
                     "—————————————————————————————————\n"
                     "Growth(last 90 days)" + self.growth + "\n"
                     "Growth Beta Worth: " + str(self.beta) +
                     "\nLowest price (last 90 days): " + str(self.lo_price) + ", date: " + self.lo_date +
                     "\nHighest price (last 90 days): " + str(self.hi_price) + ", date: " + self.hi_date)
