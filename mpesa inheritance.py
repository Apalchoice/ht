class mpesatransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process_transaction(self):
        raise NotImplementedError("subclass to use this method")


class deposittransaction(mpesatransaction):
    def process_transction(self):
        print(f"deposit transaction with ID {self.transaction_id} processed.amount{self.amount}")


class withdrawaltransaction(mpesatransaction):
    def process_transaction(self):
        print(f"withdrawal transaction with ID{self.transaction_id} processed.amount{self.amount}")


class paymenttransaction(mpesatransaction):
    def __init__(self, transaction_id, amount, recepient):
        super().__init__(transaction_id, amount)
        self.recepient = recepient


    def process_transaction(self):
        print(
            f"payment transaction with ID{self.transaction_id}process.amount {self.amount}.recepient {self.recepient}")


deposit = deposittransaction("DHTY", 2000)
withdrawal = withdrawaltransaction("GHTY", 5000)
payment = paymenttransaction("GHYT", 2000, "alex")
deposit. process_transction()
withdrawal.process_transaction()
payment.process_transaction()
