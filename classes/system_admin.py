from classes import library


class SystemAdmin:
    total_transactions = 0

    @classmethod
    def update_transactions_count(cls, amount: int=1):
        SystemAdmin.total_transactions += amount


    @classmethod
    def report_stats(cls):
        print(f'total transactions: {SystemAdmin.total_transactions} mxs borrow days: {library.Library.nax_borrow}')
