#BankExcept.py
class NameValidation(Exception):pass
class DepositError(Exception):pass
class WithDrawError(Exception):pass
class InSuffFundError(Exception):pass
class PinLengthError(Exception):pass
class CustomerNotFoundError(Exception):pass
class DuplicateAccount(Exception):pass
class SpaceError(Exception):
    pass
class EmptyNameError(Exception):
    pass
class InvalidNameError(Exception):
    pass